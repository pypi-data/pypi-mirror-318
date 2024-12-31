import pytest
from aloha_mysql.query_builder import AlohaQueryBuilder

@pytest.mark.asyncio
async def test_query_builder_select():
    """测试 SELECT 查询"""
    query = AlohaQueryBuilder('users')
    sql = str(query.select('id', 'name').where('age', '>', 18))
    expected_sql = "SELECT id, name FROM users WHERE age > '18'"
    assert sql == expected_sql

@pytest.mark.asyncio
async def test_query_builder_order_by():
    """测试 ORDER BY 子句"""
    query = AlohaQueryBuilder('users')
    sql = str(query.select('id', 'name').where('age', '>', 18).order_by('name', 'DESC'))
    expected_sql = "SELECT id, name FROM users WHERE age > '18' ORDER BY name DESC"
    assert sql == expected_sql

@pytest.mark.asyncio
async def test_query_builder_group_by():
    """测试 GROUP BY 子句"""
    query = AlohaQueryBuilder('users')
    sql = str(query.select('age', 'COUNT(*)').group_by('age'))
    expected_sql = "SELECT age, COUNT(*) FROM users GROUP BY age"
    assert sql == expected_sql

@pytest.mark.asyncio
async def test_query_builder_limit():
    """测试 LIMIT 子句"""
    query = AlohaQueryBuilder('users')
    sql = str(query.select('id', 'name').where('age', '>', 18).limit(10))
    expected_sql = "SELECT id, name FROM users WHERE age > '18' LIMIT 10"
    assert sql == expected_sql

@pytest.mark.asyncio
async def test_query_builder_insert():
    """测试 INSERT 查询"""
    query = AlohaQueryBuilder('users')
    sql = str(query.insert(id=1, name='John', age=30))
    expected_sql = "INSERT INTO users (id, name, age) VALUES ('1', 'John', '30')"
    assert sql == expected_sql

@pytest.mark.asyncio
async def test_query_builder_insert_batch():
    """测试批量插入"""
    query = AlohaQueryBuilder('users')
    sql = str(query.insert_batch(
        ['id', 'name', 'age'],
        [(1, 'Alice', 22), (2, 'Bob', 24)]
    ))
    expected_sql = "INSERT INTO users (id, name, age) VALUES ('1', 'Alice', '22'), ('2', 'Bob', '24')"
    assert sql == expected_sql

@pytest.mark.asyncio
async def test_query_builder_update():
    """测试 UPDATE 查询"""
    query = AlohaQueryBuilder('users')
    sql = str(query.update(id=1, name='John').where('age', '>', 18))
    expected_sql = "UPDATE users SET id = '1', name = 'John' WHERE age > '18'"
    assert sql == expected_sql

@pytest.mark.asyncio
async def test_query_builder_delete():
    """测试 DELETE 查询"""
    query = AlohaQueryBuilder('users')
    sql = str(query.delete().where('age', '<', 18))
    expected_sql = "DELETE FROM users WHERE age < '18'"
    assert sql == expected_sql

@pytest.mark.asyncio
async def test_query_builder_if_exist():
    """测试 IF EXISTS 查询"""
    query = AlohaQueryBuilder('users')
    sql = str(query.if_exist('age > 18'))
    expected_sql = "IF EXISTS (SELECT 1 FROM users WHERE age > 18)"
    assert sql == expected_sql

@pytest.mark.asyncio
async def test_query_builder_select_one():
    """测试 SELECT ONE 查询"""
    query = AlohaQueryBuilder('users')
    sql = str(query.select_one().select('id', 'name').where('id', '=', 1))
    expected_sql = "SELECT id, name FROM users WHERE id = '1' LIMIT 1"
    assert sql == expected_sql
