# sysobjects
## query
```sql 
-- 查看表的约束
select OBJECT_NAME(parent_obj), name, id, xtype, uid, info, type, parent_obj, crdate, sysstat, refdate, category
FROM    sysobjects
WHERE   OBJECT_NAME(parent_obj) = #{table_name};

select OBJECT_NAME(parent_obj), name, id, xtype, uid, info, type, parent_obj, crdate, sysstat, refdate, category
FROM    sysobjects
WHERE   parent_obj = object_id(#{table_name});

```

## table struct
列名 | 数据类型 | 描述
--- | --- | ---
name | sysname | 对象名,常用列
id | int | 对象标识号
xtype | char(2) | 对象类型。常用列。xtype可以是下列对象类型中的一种： C = CHECK 约束　　D = 默认值或 DEFAULT 约束　　F = FOREIGN KEY 约束　　L = 日志　　FN = 标量函数 IF = 内嵌表函数 　　P = 存储过程 　　PK = PRIMARY KEY 约束（类型是 K） 　　RF = 复制筛选存储过程 S = 系统表 　　TF = 表函数 　　TR = 触发器 　　U = 用户表 　　UQ = UNIQUE 约束（类型是 K） V = 视图 　　X = 扩展存储过程
uid | smallint | 所有者用户对象编号
info | smallint | 保留。仅限内部使用
status | int | 保留。仅限内部使用
base_schema_ ver | int | 保留。仅限内部使用
replinfo |  int | 保留。供复制使用
parent_obj |  int |  父对象的对象标识号（例如，对于触发器或约束，该标识号为表 ID）。
crdate |  datetime |  对象的创建日期。
ftcatid |  smallint |  为全文索引注册的所有用户表的全文目录标识符，对于没有注册的所有用户表则为 0
schema_ver |  int |  版本号，该版本号在每次表的架构更改时都增加。
stats_schema_ ver |  int |  保留。仅限内部使用。
type | char(2)  |  对象类型。可以是下列值之一： C = CHECK 约束   D = 默认值或 DEFAULT 约束 F = FOREIGN KEY 约束 FN = 标量函数 IF = 内嵌表函数  K = PRIMARY KEY 或 UNIQUE 约束 L = 日志 P = 存储过程 R = 规则  RF = 复制筛选存储过程 S = 系统表  TF = 表函数 TR = 触发器 U = 用户表 V = 视图 X = 扩展存储过程
userstat | smallint  |  保留。
sysstat | smallint  |  内部状态信息
indexdel |  smallint |  保留
refdate |  datetime |  留用
version | int  |  保留
deltrig  | int  |  保留
instrig | int  |  保留
updtrig | int  |  保留
seltrig | int  |  保留
category |  int |  用于发布、约束和标识
cache | smallint  |  保留

```text
type 和 xtype的区别是：
type：
K = PRIMARY KEY or UNIQUE constraint
R = Rule
xtype：
PK = PRIMARY KEY constraint (type is K)
UQ = UNIQUE constraint (type is K)

PK(xtype) + UQ(xtype) = K(type)
```

xtype_short | xtype_mean
--- | ---
AF | Aggregate function (CLR)
C | CHECK constraint
D | Default or DEFAULT constraint
F | FOREIGN KEY constraint
L | Log
FN | Scalar function
FS | Assembly (CLR) scalar-function
FT | Assembly (CLR) table-valued function
IF | In-lined table-function
IT | Internal table
P | Stored procedure
PC | Assembly (CLR) stored-procedure
PK | PRIMARY KEY constraint (type is K)
RF | Replication filter stored procedure
S | System table
SN | Synonym
SQ | Service queue
TA | Assembly (CLR) DML trigger
TF | Table function
TR | SQL DML Trigger
TT | Table type
U | User table
UQ | UNIQUE constraint (type is K)
V | View
X | Extended stored procedure

type_short | type_means
--- | ---
AF | Aggregate function (CLR)
C | CHECK constraint
D | Default or DEFAULT constraint
F | FOREIGN KEY constraint
FN | Scalar function
FS | Assembly (CLR) scalar-function
FT | Assembly (CLR) table-valued function
IF | In-lined table-function
IT | Internal table
K | PRIMARY KEY or UNIQUE constraint
L | Log
P | Stored procedure
PC | Assembly (CLR) stored-procedure
R | Rule
RF | Replication filter stored procedure
S | System table
SN | Synonym
SQ | Service queue
TA | Assembly (CLR) DML trigger
TF | Table function
TR | SQL DML Trigger
TT | Table type
U | User table
V | View
X | Extended stored procedure
