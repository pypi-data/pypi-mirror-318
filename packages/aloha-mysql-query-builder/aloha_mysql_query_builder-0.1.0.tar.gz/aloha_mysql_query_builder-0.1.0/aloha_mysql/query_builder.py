# aloha_mysql/query_builder.py

class AlohaQueryBuilder:
    def __init__(self, table):
        self.table = table
        self.columns = []
        self.conditions = []
        self.values = []
        self.query_type = None
        self.order_by_clause = None
        self.group_by_clause = None
        self.limit_clause = None

    def select(self, *args):
        """构建 SELECT 查询"""
        self.query_type = 'select'
        self.columns = args
        return self

    def where(self, column, operator, value):
        """构建 WHERE 子句"""
        if not self.query_type:
            self.query_type = 'select'
            self.columns = ['*']
        condition = f"{column} {operator} '{value}'"
        self.conditions.append(condition)
        return self

    def order_by(self, column, direction='ASC'):
        """构建 ORDER BY 子句"""
        self.order_by_clause = f"ORDER BY {column} {direction}"
        return self

    def group_by(self, *columns):
        """构建 GROUP BY 子句"""
        self.group_by_clause = f"GROUP BY {', '.join(columns)}"
        return self

    def limit(self, limit):
        """构建 LIMIT 子句"""
        self.limit_clause = f"LIMIT {limit}"
        return self

    def insert(self, **values):
        """构建 INSERT INTO 查询"""
        self.query_type = 'insert'
        self.values = values
        return self

    def insert_batch(self, columns, values_list):
        """批量插入"""
        self.query_type = 'insert_batch'
        self.columns = columns
        self.values = values_list
        return self

    def update(self, **values):
        """构建 UPDATE 查询"""
        self.query_type = 'update'
        self.values = values
        return self

    def delete(self):
        """构建 DELETE 查询"""
        self.query_type = 'delete'
        return self

    def update_batch(self, values_dict, column, value_list):
        """批量更新"""
        self.query_type = 'update_batch'
        self.values = values_dict
        # 确保 IN 子句中的值被正确格式化为字符串，并加上单引号
        formatted_values = [f"'{value}'" for value in value_list]
        self.conditions.append(f"{column} IN ({', '.join(formatted_values)})")
        return self

    def if_exist(self, condition):
        """构建 IF EXISTS 查询"""
        self.query_type = 'if_exist'
        self.conditions.append(condition)
        return self

    def select_one(self):
        """构建 SELECT ONE 查询（仅返回一条记录）"""
        self.limit(1)
        return self

    def __str__(self):
        """生成最终的 SQL 查询"""
        sql = ""  # 初始化sql变量，以防某些条件不匹配

        if self.query_type == 'select':
            # 处理 SELECT 查询
            columns = ', '.join(self.columns)
            sql = f"SELECT {columns} FROM {self.table}"
            if self.conditions:
                sql += " WHERE " + " AND ".join(self.conditions)
            if self.group_by_clause:
                sql += " " + self.group_by_clause
            if self.order_by_clause:
                sql += " " + self.order_by_clause
            if self.limit_clause:
                sql += " " + self.limit_clause

        elif self.query_type == 'insert':
            # 处理单个插入（INSERT）
            if isinstance(self.values, dict):
                # 如果插入的值是字典
                columns = ', '.join(self.values.keys())
                vals = ', '.join([f"'{v}'" for v in self.values.values()])
                sql = f"INSERT INTO {self.table} ({columns}) VALUES ({vals})"
            else:
                # 否则，插入的值是元组列表
                sql = f"INSERT INTO {self.table} ({', '.join(self.columns)}) " \
                      f"VALUES ({', '.join([f'({', '.join([str(x) if isinstance(x, (int, float)) else f'\'{x}\'' for x in value])})' for value in self.values])})"

        elif self.query_type == 'insert_batch':
            # 处理批量插入（INSERT）
            formatted_values = ', '.join([
                f"({', '.join([f'\'{x}\'' for x in value])})"
                for value in self.values
            ])
            sql = f"INSERT INTO {self.table} ({', '.join(self.columns)}) VALUES {formatted_values}"

        elif self.query_type == 'update':
            # 处理更新（UPDATE）
            set_clause = ', '.join([f"{k} = '{v}'" for k, v in self.values.items()])
            sql = f"UPDATE {self.table} SET {set_clause}"
            if self.conditions:
                sql += " WHERE " + " AND ".join(self.conditions)

        elif self.query_type == 'update_batch':
            # 处理批量更新（UPDATE）
            set_clause = ', '.join([f"{k} = '{v}'" for k, v in self.values.items()])
            sql = f"UPDATE {self.table} SET {set_clause}"
            if self.conditions:
                sql += " WHERE " + " AND ".join(self.conditions)

        elif self.query_type == 'delete':
            # 处理删除（DELETE）
            if self.conditions:
                sql = f"DELETE FROM {self.table} WHERE " + " AND ".join(self.conditions)
            else:
                sql = f"DELETE FROM {self.table}"

        elif self.query_type == 'if_exist':
            # 处理 IF EXISTS 查询
            sql = f"IF EXISTS (SELECT 1 FROM {self.table} WHERE " + " AND ".join(self.conditions) + ")"

        elif self.query_type == 'select_one':
            # 处理 SELECT ONE 查询
            columns = ', '.join(self.columns)
            sql = f"SELECT {columns} FROM {self.table}"
            if self.conditions:
                sql += " WHERE " + " AND ".join(self.conditions)
            sql += " LIMIT 1"

        else:
            # 默认情况下，如果只有 WHERE 条件，但未设置查询类型，假设 SELECT *
            if self.conditions:
                sql = f"SELECT * FROM {self.table} WHERE " + " AND ".join(self.conditions)
            else:
                # 默认 SELECT *
                sql = f"SELECT * FROM {self.table}"

        return sql
