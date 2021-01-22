# oracle procedure
## query procedure
``` sql
-- 查询一个用户中存在的过程
select object_name,created,status 
from user_objects 
where lower(object_type) in ('procedure');  

-- 查询过程的代码
select * 
from user_source 
where name in (
	SELECT name
	FROM user_source 
	WHERE TYPE IN('PROCEDURE') and lower(text) like '%#{search_content}%'
);
```