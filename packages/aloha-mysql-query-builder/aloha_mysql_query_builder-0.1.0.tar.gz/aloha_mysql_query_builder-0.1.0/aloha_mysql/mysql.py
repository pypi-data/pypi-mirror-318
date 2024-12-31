# aloha_mysql/mysql.py

import aiomysql


class AlohaMySQL:
    def __init__(self, host, port, user, password, db, minsize=1, maxsize=10):
        """
        初始化 AlohaMySQL 实例。

        :param host: 数据库主机
        :param port: 数据库端口
        :param user: 用户名
        :param password: 密码
        :param db: 数据库名称
        :param minsize: 最小连接池大小
        :param maxsize: 最大连接池大小
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.pool = None
        self.minsize = minsize
        self.maxsize = maxsize

    async def init_pool(self):
        """
        初始化连接池
        """
        self.pool = await aiomysql.create_pool(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset='utf8mb4',
            minsize=self.minsize,
            maxsize=self.maxsize
        )

    async def _fetchone(self, query, params):
        """
        执行查询，返回单条记录

        :param query: SQL 查询语句
        :param params: 查询参数
        :return: 返回查询结果
        """
        async with self.pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(query, params)
                return await cursor.fetchone()

    async def _fetchall(self, query, params=None):
        """
        执行查询，返回所有记录

        :param query: SQL 查询语句
        :param params: 查询参数
        :return: 返回查询结果
        """
        async with self.pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(query, params)
                return await cursor.fetchall()
