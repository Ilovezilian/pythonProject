# sql server table
## delete 
```sql 
alter table #{table_name} drop column #{column_name}
alter table #{table_name} drop constraint #{constraint_name}
```

## query

```sql 
-- 查看约束
select  *
from    sysobjects
where   object_name(parent_obj) = #{table_name}

select  *
from    sysobjects
where   parent_obj = object_id(#{table_name})
```