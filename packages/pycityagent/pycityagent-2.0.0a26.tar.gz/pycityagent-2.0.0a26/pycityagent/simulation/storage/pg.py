import asyncio
from collections import defaultdict
from typing import Any

import psycopg
import psycopg.sql
import ray
from psycopg.rows import dict_row

from ...utils.decorators import lock_decorator
from ...utils.pg_query import PGSQL_DICT


def create_pg_tables(exp_id: str, dsn: str):
    for table_type, exec_strs in PGSQL_DICT.items():
        table_name = f"socialcity_{exp_id.replace('-', '_')}_{table_type}"
        # # debug str
        # for _str in [f"DROP TABLE IF EXISTS {table_name}"] + [
        #     _exec_str.format(table_name=table_name) for _exec_str in exec_strs
        # ]:
        #     print(_str)
        with psycopg.connect(dsn) as conn:
            with conn.cursor() as cur:
                # delete table
                cur.execute(f"DROP TABLE IF EXISTS {table_name}")  # type:ignore
                conn.commit()
                # create table
                for _exec_str in exec_strs:
                    cur.execute(_exec_str.format(table_name=table_name))
                conn.commit()


@ray.remote
class PgWriter:
    def __init__(self, exp_id: str, dsn: str):
        self.exp_id = exp_id
        self._dsn = dsn
        # self._lock = asyncio.Lock()

    # @lock_decorator
    async def async_write_dialog(self, rows: list[tuple]):
        _tuple_types = [str, int, float, int, str, str, str, None]
        table_name = f"socialcity_{self.exp_id.replace('-', '_')}_agent_dialog"
        # 将数据插入数据库
        async with await psycopg.AsyncConnection.connect(self._dsn) as aconn:
            copy_sql = psycopg.sql.SQL(
                "COPY {} (id, day, t, type, speaker, content, created_at) FROM STDIN"
            ).format(psycopg.sql.Identifier(table_name))
            async with aconn.cursor() as cur:
                async with cur.copy(copy_sql) as copy:
                    for row in rows:
                        _row = [
                            _type(r) if _type is not None else r
                            for (_type, r) in zip(_tuple_types, row)
                        ]
                        await copy.write_row(_row)

    # @lock_decorator
    async def async_write_status(self, rows: list[tuple]):
        _tuple_types = [str, int, float, float, float, int, str, str, None]
        table_name = f"socialcity_{self.exp_id.replace('-', '_')}_agent_status"
        async with await psycopg.AsyncConnection.connect(self._dsn) as aconn:
            copy_sql = psycopg.sql.SQL(
                "COPY {} (id, day, t, lng, lat, parent_id, action, status, created_at) FROM STDIN"
            ).format(psycopg.sql.Identifier(table_name))
            async with aconn.cursor() as cur:
                async with cur.copy(copy_sql) as copy:
                    for row in rows:
                        _row = [
                            _type(r) if _type is not None else r
                            for (_type, r) in zip(_tuple_types, row)
                        ]
                        await copy.write_row(_row)

    # @lock_decorator
    async def async_write_profile(self, rows: list[tuple]):
        _tuple_types = [str, str, str]
        table_name = f"socialcity_{self.exp_id.replace('-', '_')}_agent_profile"
        async with await psycopg.AsyncConnection.connect(self._dsn) as aconn:
            copy_sql = psycopg.sql.SQL("COPY {} (id, name, profile) FROM STDIN").format(
                psycopg.sql.Identifier(table_name)
            )
            async with aconn.cursor() as cur:
                async with cur.copy(copy_sql) as copy:
                    for row in rows:
                        _row = [
                            _type(r) if _type is not None else r
                            for (_type, r) in zip(_tuple_types, row)
                        ]
                        await copy.write_row(_row)

    # @lock_decorator
    async def async_write_survey(self, rows: list[tuple]):
        _tuple_types = [str, int, float, str, str, None]
        table_name = f"socialcity_{self.exp_id.replace('-', '_')}_agent_survey"
        async with await psycopg.AsyncConnection.connect(self._dsn) as aconn:
            copy_sql = psycopg.sql.SQL(
                "COPY {} (id, day, t, survey_id, result, created_at) FROM STDIN"
            ).format(psycopg.sql.Identifier(table_name))
            async with aconn.cursor() as cur:
                async with cur.copy(copy_sql) as copy:
                    for row in rows:
                        _row = [
                            _type(r) if _type is not None else r
                            for (_type, r) in zip(_tuple_types, row)
                        ]
                        await copy.write_row(_row)

    # @lock_decorator
    async def async_update_exp_info(self, exp_info: dict[str, Any]):
        # timestamp不做类型转换
        TO_UPDATE_EXP_INFO_KEYS_AND_TYPES = [
            ("id", str),
            ("name", str),
            ("num_day", int),
            ("status", int),
            ("cur_day", int),
            ("cur_t", float),
            ("config", str),
            ("error", str),
            ("created_at", None),
            ("updated_at", None),
        ]
        table_name = f"socialcity_{self.exp_id.replace('-', '_')}_experiment"
        async with await psycopg.AsyncConnection.connect(self._dsn) as aconn:
            async with aconn.cursor(row_factory=dict_row) as cur:
                # UPDATE
                columns = ", ".join(
                    f"{key} = %s" for key, _ in TO_UPDATE_EXP_INFO_KEYS_AND_TYPES
                )
                update_sql = psycopg.sql.SQL(
                    f"UPDATE {{}} SET {columns} WHERE id = %s"  # type:ignore
                ).format(psycopg.sql.Identifier(table_name))
                params = [
                    _type(exp_info[key]) if _type is not None else exp_info[key]
                    for key, _type in TO_UPDATE_EXP_INFO_KEYS_AND_TYPES
                ] + [self.exp_id]
                await cur.execute(update_sql, params)
                await aconn.commit()
