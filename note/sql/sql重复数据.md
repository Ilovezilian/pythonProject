# sql 语句查询表中重复数据（多类型）
> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.cnblogs.com](https://www.cnblogs.com/he1234/p/15900980.html)

表名：hztj

字段名：edxzqhdm ,sdxzqhdm

## sql 语句查询表中重复数据（多类型）
1. 查出某一列数据中重复的，以 sdxzqhdm 为例

```sql
select * 
from hztj a where (a.sdxzqhdm) in (
select sdxzqhdm  
from hztj group by sdxzqhdm having count(*) > 1
)
```
2. 查询出所有数据进行分组之后，和重复数据的重复次数的查询数据

```sql
select count(sdxzqhdm) as '重复次数',sdxzqhdm 
from hztj 
group by sdxzqhdm 
having count(*)>1 
order by sdxzqhdm desc

```

## 查询及删除重复记录的方法

1. 查找表中多余的重复记录，重复记录是根据单个字段来判断 ，如：

```sql
select * 
from hztj
where sdxzqhdm in (
	select sdxzqhdm from hztj group by sdxzqhdm having count(sdxzqhdm) > 1
)

```

2. 删除表中多余的重复记录，重复记录是根据单个字段来判断，只留 rowid 最小的记录

```sql
delete from hztj
where sdxzqhdm in (
	select sdxzqhdm from hzth group  by  sdxzqhdm having  count(sdxzqhdm) > 1
)
and rowid not in (
	select min(rowid) from  hztj group by sdxzqhdm having count(sdxzqhdm)>1
)

```

3. 查找表中多余的重复记录（多个字段）

```sql
select * from hztj a
where (a.sdxzqhdm,a.edxzqhdm) in (
	select sdxzqhdm,edxzqhdm from hztj group by sdxzqhdm,edxzqhdm having count(*) > 1
)

```

4. 删除表中多余的重复记录（多个字段），只留有 rowid 最小的记录

```sql
delete from hztj a
where (a.sdxzqhdm,a.edxzqhdm) in (
	select sdxzqhdm,edxzqhdm from hztj group by sdxzqhdm,edxzqhdm having count(*) > 1
) 
and rowid not in (
	select min(rowid) from hztj group by sdxzqhdm,edxzqhdm having count(*)>1
)

```

5. 查找表中多余的重复记录（多个字段），不包含 rowid 最小的记录

```sql
select * from hztj a
where (a.sdxzqhdm,a.edxzqhdm) in  (
	select sdxzqhdm,edxzqhdm from hztj group by sdxzqhdm,edxzqhdm having count(*) > 1
)
and rowid not in (
	select min(rowid) from hztj group by sdxzqhdm,edxzqhdm having count(*)>1
)

```