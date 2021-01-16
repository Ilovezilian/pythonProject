# oracle index
### 1、创建单一索引
```sql
create index 索引名称 on 表名(列名);

create index attencefile_index3 on T_HR_ATS_ATTENDANCEFILE(FADMINORGUNITID , FPROPOSERID , FATTENDFILESTATE, FISATTENDANCE);
```
### 2、创建复合索引
```sql
create index 索引名称 on 表名(列名1,列名2);
```
### 3、删除索引
```sql
drop index 索引名称;
```
### 4、查询表的索引
```sql
-- 查询出表的索引(用户）
select * from user_indexes where table_name = upper('表名称');
-- 查询出表的索引(所有）
select * from all_indexes where table_name = upper('表名称')  and OWNER = upper('库名称');
select * from all_indexes where table_name = upper('T_HR_ATS_SCHEDULESHIFT') and OWNER = 'OPPO861PATCH';

-- 查询用户表的索引(非聚集索引): 
select * from user_indexes where uniqueness='NONUNIQUE'

-- 查询用户表的主键(聚集索引): 
select * from user_indexes where uniqueness='UNIQUE'

-- 查询表的索引(用户)
select t.*,i.* from user_ind_columns t,user_indexes i where t.index_name = i.index_name and t.table_name=upper('表名称');

select t.*,i.* from user_ind_columns t,user_indexes i where t.index_name = i.index_name and t.table_name=upper('表名称');


-- 查询表的索引（所有）
select t.*,i.* from all_ind_columns t,all_indexes i where t.index_name = i.index_name and t.table_name=upper('表名称');
```

### 5、查询表的索引列
```sql
select* from all_ind_columns where table_name = upper('表名称');
```

### 6、重建索引

```sql 
alter index '索引名称' rebuild
```
### 查看索引个数和类别

```sql 
select * from user_indexes where table_name=upper('表名');
```

### 碎片化分析
```sql  
analyze index '索引名' validate structure;
-- 如：
analyze index OPPODATA0125.INDEX_SCHEDULE_PERSONID2 validate structure;

-- 下面是固定句式，上面执行完之后name就会显示 索引名称；
select name,del_lf_rows_len,lf_rows_len,(del_lf_rows_len/lf_rows_len)*100 as "索引碎片率" from index_stats;
```

