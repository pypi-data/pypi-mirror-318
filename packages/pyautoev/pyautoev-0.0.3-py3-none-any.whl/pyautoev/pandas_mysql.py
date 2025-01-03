# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine


class pd_mysql(object):
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def fetch_all(self, sql, *args):
        """
        批量查询
        :param sql: SQL 查询语句
        :param args: 参数列表
        :return: DataFrame
        """
        # 使用 pandas 的 read_sql 方法执行查询
        df = pd.read_sql(sql, self.engine, params=args if args else None)
        return df

    def fetch_one(self, sql, *args):
        """
        查询单条数据
        :param sql: SQL 查询语句
        :param args: 参数列表
        :return: 单条记录
        """
        df = self.fetch_all(sql, *args)
        # 返回第一条记录，如果不存在则返回 None
        return df.iloc[0] if not df.empty else None

    def execute_sql(self, sql, *args):
        """
        执行 SQL 语句
        :param sql: SQL 执行语句
        :param args: 参数列表
        :return: 受影响的行数
        """
        with self.engine.connect() as connection:
            result = connection.execute(sql, *args)
            return result.rowcount

    def database_name(self):
        """
        获取数据库名
        :return: 数据库名
        """
        return self.engine.url.database


# 使用示例
# db_connection_string = 'mysql+pymysql://user:password@host:port/database'
# db_tools = MySQLTools(db_connection_string)
# 查询示例
# all_records = db_tools.fetch_all("SELECT * FROM your_table")
# print(all_records)
