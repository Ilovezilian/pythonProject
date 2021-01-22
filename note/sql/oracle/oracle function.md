## oracle function
## query function
``` sql
-- 查询一个用户中存在的函数
select object_name,created,status from user_objects where lower(object_type) in ('function');  

-- 查询函数的代码
select * 
from user_source 
where name in (
	SELECT name
	FROM user_source 
	WHERE TYPE IN('FUNCTION') and lower(text) like '%#{search_content}%'
);
```
