# 后端事务处理相关
### 根据实例标题查看内容
可以取后台事务实例表查数据，查到的结果右键导出到excel发来看看：
```sql
SELECT * FROM T_JOB_INST where FTITLE like '%【这里内容改成你要查的后台事务实例标题】%'
```
SELECT * FROM T_JOB_INST where FTITLE like '%自动排班%'
