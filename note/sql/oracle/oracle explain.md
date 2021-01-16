# oracle explain
```sql 
EXPLAIN PLAN FOR 
待执行的sql;
--（不要忘了分号）
SELECT * FROM TABLE (dbms_xplan.display());
也可以使用下面这条，会显示更多信息：
SELECT * FROM TABLE (dbms_xplan.display(null,null,'advanced'));
```