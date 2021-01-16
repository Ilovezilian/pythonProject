## oracle table

### query
```sql
-- 查询表（用户）
select * from user_tables where table_name = upper('表名称');
--  查询表（所有）
select * from all_tables where table_name = upper('表名称');

-- 查询表的主键（用户）
select cu.* 
from user_cons_columns cu, user_constraints au 
where cu.constraint_name = au.constraint_name and au.constraint_type = 'P' AND cu.table_name = upper('表名称');

-- 查询表的主键（所有）
select cu.* 
from all_cons_columns cu, all_constraints au 
where cu.constraint_name = au.constraint_name and au.constraint_type = 'P' AND cu.table_name = upper('表名称') AND cu.OWNER = upper('库名称');

-- 查询表的所有列及其属性
select * from user_tab_columns where table_name=upper('表名');
select cname,coltype,width from col where tname=upper('表名');;  
```
