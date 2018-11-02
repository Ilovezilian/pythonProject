# mysql optimizing
## Optimizing SELECT Statements
### The main considerations for optimizing queries are:
To make a slow SELECT ... WHERE query faster, the first thing to check is whether you can add an index. Set up indexes on columns used in the WHERE clause, to speed up evaluation, filtering, and the final retrieval of results. To avoid wasted disk space, construct a small set of indexes that speed up many related queries used in your application.

在where语句下面使用索引进行筛选

Indexes are especially important for queries that reference different tables, using features such as joins and foreign keys. You can use the EXPLAIN statement to determine which indexes are used for a SELECT. See Section 8.3.1, “How MySQL Uses Indexes” and Section 8.8.1, “Optimizing Queries with EXPLAIN”.

连表查询on条件使用索引

Isolate and tune any part of the query, such as a function call, that takes excessive time. Depending on how the query is structured, a function could be called once for every row in the result set, or even once for every row in the table, greatly magnifying any inefficiency.

尽量不在查询中使用函数，否则函数会运行全表的数据，那耗时就相当可观了。

Minimize the number of full table scans in your queries, particularly for big tables.

尽量避免全表查询，尤其是大表。

Keep table statistics up to date by using the ANALYZE TABLE statement periodically, so the optimizer has the information needed to construct an efficient execution plan.

定期检查，进行优化计划

Learn the tuning techniques, indexing techniques, and configuration parameters that are specific to the storage engine for each table. Both InnoDB and MyISAM have sets of guidelines for enabling and sustaining high performance in queries. For details, see Section 8.5.6, “Optimizing InnoDB Queries” and Section 8.6.1, “Optimizing MyISAM Queries”.

You can optimize single-query transactions for InnoDB tables, using the technique in Section 8.5.3, “Optimizing InnoDB Read-Only Transactions”.

Avoid transforming the query in ways that make it hard to understand, especially if the optimizer does some of the same transformations automatically.

If a performance issue is not easily solved by one of the basic guidelines, investigate the internal details of the specific query by reading the EXPLAIN plan and adjusting your indexes, WHERE clauses, join clauses, and so on. (When you reach a certain level of expertise, reading the EXPLAIN plan might be your first step for every query.)

使用执行计划，进行表结构、索引、以及连表等调优

Adjust the size and properties of the memory areas that MySQL uses for caching. With efficient use of the InnoDB buffer pool, MyISAM key cache, and the MySQL query cache, repeated queries run faster because the results are retrieved from memory the second and subsequent times.


Even for a query that runs fast using the cache memory areas, you might still optimize further so that they require less cache memory, making your application more scalable. Scalability means that your application can handle more simultaneous users, larger requests, and so on without experiencing a big drop in performance.

Deal with locking issues, where the speed of your query might be affected by other sessions accessing the tables at the same time.

## Optimizing Subqueries, Derived Tables, View References, and Common Table Expressions
## Optimizing INFORMATION_SCHEMA Queries
## Optimizing Performance Schema Queries
## Optimizing Data Change Statements
## Optimizing Database Privileges
## Other Optimization Tips
