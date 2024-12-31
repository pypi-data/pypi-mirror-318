# Aloha MySQL Query Builder

Aloha MySQL Query Builder 是一个 Python 库，用于简化 MySQL 查询的构建，支持构建常见的 SQL 查询语句，包括 SELECT、INSERT、UPDATE、DELETE 等。该库提供了一个简洁的 API，使得在 Python 中构建和执行 MySQL 查询变得更加方便。

## 特性

- 支持 `SELECT`, `INSERT`, `UPDATE`, `DELETE` 等常见 SQL 查询类型。
- 支持 `WHERE`, `ORDER BY`, `GROUP BY`, `LIMIT` 等 SQL 子句。
- 支持批量插入和批量更新。
- 支持构建完整的 SQL 查询字符串，便于执行。
- 支持检查记录是否存在（`IF EXISTS`）。
- 支持仅返回一条记录的查询（`SELECT ONE`）。

## 安装

你可以通过 `pip` 安装 Aloha MySQL Query Builder：

```bash
pip install aloha-mysql-query-builder
```

## 用法

### 1. 基本用法

#### 1.1 SELECT 查询

```python
from aloha_mysql.query_builder import AlohaQueryBuilder

query = AlohaQueryBuilder('users')
query = query.select('id', 'name').where('age', '>', 18)
sql = str(query)
print(sql)  # 输出: SELECT id, name FROM users WHERE age > '18'
```

#### 1.2 INSERT 查询

```python
query = AlohaQueryBuilder('users')
query = query.insert(id=1, name='John', age=30)
sql = str(query)
print(sql)  # 输出: INSERT INTO users (id, name, age) VALUES ('1', 'John', '30')
```

#### 1.3 UPDATE 查询

```python
query = AlohaQueryBuilder('users')
query = query.update(name='John Doe', age=31).where('id', '=', 1)
sql = str(query)
print(sql)  # 输出: UPDATE users SET name = 'John Doe', age = '31' WHERE id = '1'
```

#### 1.4 DELETE 查询

```python
query = AlohaQueryBuilder('users')
query = query.delete().where('age', '<', 18)
sql = str(query)
print(sql)  # 输出: DELETE FROM users WHERE age < '18'
```

### 2. 高级用法

#### 2.1 批量插入

```python
query = AlohaQueryBuilder('users')
query = query.insert_batch(
    ['id', 'name', 'age'],  # 明确列名
    [(1, 'Alice', 22), (2, 'Bob', 24)]
)
sql = str(query)
print(sql)  # 输出: INSERT INTO users (id, name, age) VALUES ('1', 'Alice', '22'), ('2', 'Bob', '24')
```

#### 2.2 批量更新

```python
query = AlohaQueryBuilder('users')
query = query.update_batch(
    {'name': 'John Doe', 'age': 31},
    'id',
    [1, 2, 3]
)
sql = str(query)
print(sql)  # 输出: UPDATE users SET name = 'John Doe', age = '31' WHERE id IN ('1', '2', '3')
```

### 3. 添加排序、分组和限制

#### 3.1 添加排序 (ORDER BY)

```python
query = AlohaQueryBuilder('users')
query = query.select('id', 'name').where('age', '>', 18).order_by('age', 'DESC')
sql = str(query)
print(sql)  # 输出: SELECT id, name FROM users WHERE age > '18' ORDER BY age DESC
```

#### 3.2 添加分组 (GROUP BY)

```python
query = AlohaQueryBuilder('users')
query = query.select('age', 'COUNT(*)').group_by('age')
sql = str(query)
print(sql)  # 输出: SELECT age, COUNT(*) FROM users GROUP BY age
```

#### 3.3 添加限制 (LIMIT)

```python
query = AlohaQueryBuilder('users')
query = query.select('id', 'name').limit(10)
sql = str(query)
print(sql)  # 输出: SELECT id, name FROM users LIMIT 10
```

### 4. 其他功能

#### 4.1 `select_one` 方法

```python
query = AlohaQueryBuilder('users')
query = query.select_one().select('id', 'name').where('id', '=', 1)
sql = str(query)
print(sql)  # 输出: SELECT id, name FROM users WHERE id = '1' LIMIT 1
```

#### 4.2 `if_exist` 方法

```python
query = AlohaQueryBuilder('users')
query = query.if_exist('age > 18')
sql = str(query)
print(sql)  # 输出: IF EXISTS (SELECT 1 FROM users WHERE age > 18)
```

## 运行测试

运行 `pytest` 来执行单元测试：

```bash
pytest tests/
```

## 贡献

欢迎提交 Issues 或 Pull Requests，参与改进本项目。

## License

Aloha MySQL Query Builder 使用 MIT 许可证。详细信息请参阅 LICENSE 文件。
