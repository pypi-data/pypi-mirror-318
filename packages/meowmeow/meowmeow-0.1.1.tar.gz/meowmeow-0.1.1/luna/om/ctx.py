import json
import logging
from contextlib import asynccontextmanager
from datetime import datetime
from decimal import Decimal
from functools import cached_property
from pathlib import Path
from typing import (
    Any,
)

import pendulum
from psycopg import AsyncConnection, AsyncCursor
from psycopg.rows import dict_row
from psycopg.types.json import Json
from psycopg_pool import AsyncConnectionPool

from luna.sql.base import AbstractSqlBlock
from luna.sql.ctx import SqlGenContext

from .meta import Omt

parent_dir = Path(__file__).parent
log = logging.getLogger(__name__)


def default_json(v: Any) -> Any:
    if isinstance(v, Decimal):
        return str(v)
    if isinstance(v, datetime):
        return v.isoformat()
    raise TypeError(f"Unsupported type: {type(v)}")


def dump_json(v: Any) -> str:
    return json.dumps(v, default=default_json)


class SqlContext(SqlGenContext):
    def __init__(self, pool: AsyncConnectionPool = None, schema: str = "public"):
        search_paths = [parent_dir / "templates"]
        super().__init__(search_paths=search_paths)
        self.schema = schema
        self.pool = pool
        self._cursor: AsyncCursor = None
        self._conn: AsyncConnection = None

    def get_fqtn(self, table_name: str) -> str:
        return self.quote(self.schema) + "." + self.quote(table_name)

    @property
    def cursor(self):
        assert self._cursor is not None, "Cursor not available"
        return self._cursor

    @property
    def connection(self):
        assert self._conn is not None, "Connection not available"
        return self._conn

    @asynccontextmanager
    async def use_db(self, start_transaction: bool = False):
        """Prepare the connections and cursor for a transaction"""
        pool = self.pool
        await pool.open()
        async with pool.connection() as conn:
            self._conn = conn
            conn.row_factory = dict_row
            cursor = conn.cursor()
            async with cursor:
                self._cursor = cursor
                if start_transaction:
                    await cursor.execute("begin transaction")
                try:
                    yield cursor
                    await conn.commit()
                except Exception:
                    await conn.rollback()
                    raise

    async def run_query(
        self,
        template: str = None,
        query: str | AbstractSqlBlock = None,
        many=False,
        params=None,
        exec: bool = False,
        **kwargs,
    ):
        if query is not None:
            if isinstance(query, AbstractSqlBlock):
                query = query.to_sql(self)
        else:
            query = self.render_template(template, **kwargs)
        log.debug("Query: %s", query)
        await self.cursor.execute(query, params)
        if exec:
            return
        result = list(await self.cursor.fetchall())
        if many:
            return result
        else:
            assert len(result) < 2
            if len(result) == 0:
                return None
            return result[0]

    @cached_property
    def now(self):
        return pendulum.now(tz=pendulum.UTC)

    async def start_transaction(self):
        await self.cursor.execute("BEGIN TRANSACTION")

    async def commit(self):
        await self.connection.commit()

    def serialize(self, om: Omt, value: Any):
        om: Omt
        if value is None:
            return None
        if om.info.annotation is None:
            return value
        if om.info.annotation in (int, float, bool, str):
            return value
        elif om.info.annotation == Decimal:
            return Decimal(value) if not isinstance(value, Decimal) else value
        elif om.info.annotation == datetime:
            return value
        elif om.to_db_value is not None:
            return om.to_db_value(value)
        elif om.is_json:
            return Json(value, dumps=dump_json)
        return value
        # Optional[datetime] ???
        # should return something before this
        raise NotImplementedError(f"Unsupported type: {om.info}")


# re-export for type hinting
def use_sql_context() -> SqlContext:
    from luna.sql.ctx import use_sql_context

    ctx = use_sql_context()
    assert isinstance(ctx, SqlContext)
    return ctx


def set_sql_context(sql: SqlContext):
    from luna.sql.ctx import set_sql_context

    sql: SqlGenContext
    return set_sql_context(sql)


# def use_db(start_transaction=False):
#     """Prepare the current context for database operations which makes cursor and connection available"""

#     def decorator(func):
#         async def wrapper(*args, **kwargs):
#             ctx = use_sql_context()
#             async with ctx.use_db(start_transaction=start_transaction):
#                 res = await func(*args, **kwargs)
#             return res

#         return wrapper

#     return decorator
