# primary query
## 分页查询
```sql 
SELECT * FROM test_table WHERE i_id>1000 order by i_id  limit 100;

SELECT * FROM test_table order by i_id limit 100 OFFSET 1000;
```