# oracle procedure
## query procedure
``` sql
-- 查询一个用户中存在的过程和函数
select object_name,created,status from user_objects where lower(object_type) in ('procedure');  
```