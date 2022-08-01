from typing import Union

import asyncpg

from data import config


class Database:

    def __init__(self):
        self.pool: Union[asyncpg.Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: asyncpg.Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    @staticmethod
    def format_args(sql, param: dict):
        sql += " AND ".join([f"{item} = ${num}" for num, item in enumerate(param.keys(), start=1)])
        return sql, tuple(param.values())

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE, 
        phone_number VARCHAR(255) NULL    
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_msg(self):
        sql = """
        CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        telegram_id BIGINT NOT NULL,
        date TIMESTAMP NOT NULL,
        message VARCHAR(255) NULL
        ); 
        """
        await self.execute(sql, execute=True)

    async def check_lists_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS lists (
        id SERIAL PRIMARY KEY,
        hashtag1 VARCHAR(255) NOT NULL,
        hashtag2 VARCHAR(255) NOT NULL,
        outside1 VARCHAR(255) NOT NULL,
        outside2 VARCHAR(255) NOT NULL
        );
        """
        await self.execute(sql, execute=True)

    async def money_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS money (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NOT NULL,
        money VARCHAR(255) NULL,
        date TIMESTAMP NOT NULL
        ); 
        """
        await self.execute(sql, execute=True)

    async def add_user(self, full_name, username, telegram_id, phone_number):
        sql = """
        INSERT INTO users (full_name, username, telegram_id, phone_number)
        VALUES ($1, $2, $3, $4);
        """
        try:
            await self.execute(sql, full_name, username, telegram_id, phone_number, execute=True)
        except Exception as e:
            print(e)

    async def message(self, full_name, telegram_id, date, message):
        sql = """
        INSERT INTO messages (full_name, telegram_id, date, message)
        VALUES ($1, $2, $3, $4);
        """
        try:
            await self.execute(sql, full_name, telegram_id, date, message, execute=True)
        except Exception as e:
            print(e)

    async def add_money(self, money, telegram_id, date):
        sql = """
        INSERT INTO money (telegram_id, money, date)
        VALUES ($1, $2, $3);
        """
        try:
            await self.execute(sql, money, telegram_id, date, execute=True)
        except Exception as e:
            print(e)

    async def get_money(self, telegram_id) -> dict:
        sql = """
        SELECT money, date FROM money WHERE telegram_id = $1;
        """
        try:
            result = await self.execute(sql, telegram_id, fetch=True)
            result = {item[1]: item[0] for item in result}
            return result
        except Exception as e:
            print(e)

    async def update_check_lists(self, hashtag1, hashtag2, outside1, outside2, id):
        try:
            sql = """
            UPDATE lists SET hashtag1 = $1, hashtag2 = $2, outside1 = $3, outside2 = $4
            WHERE id = $5;
            """
            await self.execute(sql, hashtag1, hashtag2, outside1, outside2, id, execute=True)
        except Exception as e:
            print(e)

    async def get_check_lists(self):
        sql = """
        SELECT hashtag1, hashtag2, outside1, outside2 FROM lists WHERE id = 1;
        """
        try:
            result = await self.execute(sql, fetch=True)
            return result
        except Exception as e:
            print(e)

    async def get_close_lists(self):
        sql = """
        SELECT hashtag1, hashtag2, outside1, outside2 FROM lists WHERE id = 2;
        """
        try:
            result = await self.execute(sql, fetch=True)
            return result
        except Exception as e:
            print(e)
