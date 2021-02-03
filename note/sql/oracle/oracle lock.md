# oracle lock
## type
* exclusive locks 独占锁
* share locks 共享锁

## Locks achieve the following important database requirements
* Consistency 一致性
* Integrity 完整性

## Lock Modes
* Exclusive lock mode 独占模式
* Share lock mode 共享模式

## Lock Conversion and Escalation
### Lock Conversion 锁转换
Oracle Database performs lock conversion as necessary. In lock conversion, the
database automatically converts a table lock of lower restrictiveness to one of higher
restrictiveness.

锁转换把锁的进行更高的约束转换（如 表锁到行锁）
### Lock Escalation 锁升级
Lock conversion is different from lock escalation, which occurs when numerous locks
are held at one level of granularity (for example, rows) and a database raises the locks
to a higher level of granularity (for example, table)
锁转换不同于锁升级，后者发生在多个锁的情况下，在一个粒度级别(例如，行)被持有，数据库引发锁到更高级别的粒度(例如，表)
一个用户持有一个表的多个行锁，会导致升级为拥有该表的表锁

## Locks and Deadlocks
A deadlock is a situation in which two or more users are waiting for data locked by
each other. Deadlocks prevent some transactions from continuing to work.
死锁是多个用户同时等待对方已经锁定的资源。死锁会阻碍了事务继续工作。

Oracle Database automatically detects deadlocks and resolves them by rolling back
one statement involved in the deadlock, releasing one set of the conflicting row locks.
Oracle数据库会自动发现死锁并且通过回滚一个或者多个导致死锁的的行锁的语句进行解决。

## Locks Categories
Lock | Description
--- | ---
DML | Locks Protect data. For example, table locks lock entire tables, while row locks lock selected rows. See "DML Locks" on page 9-18.
DDL | Locks Protect the structure of schema objects—for example, the dictionary definitions of tables and views. See "DDL Locks" on page 9-24.
System Locks | Protect internal database structures such as data files. Latches, mutexes, and internal locks are entirely automatic. See "System Locks" on page 9-25.

## systemLocks
### Latches 闩锁
Latches are simple, low-level serialization mechanisms that coordinate multiuser
access to shared data structures, objects, and files. Latches protect shared memory
resources from corruption when accessed by multiple processes. 
锁存是协调多用户的简单、低级的序列化机制访问共享的数据结构、对象和文件。锁存器保护共享内存资源在被多个进程访问时不会损坏

* Concurrent modification by multiple sessions 多个会话同时修改
* Being read by one session while being modified by another session 由一个会话读取，同时由另一个会话修改
* Deallocation (aging out) of memory while being accessed 在被访问时释放内存(老化)

### Mutexes 互斥对象锁
A **mutual exclusion object (mutex)** is a low-level mechanism that prevents an object in
memory from aging out or from being corrupted when accessed by concurrent
processes. A mutex is similar to a latch, but whereas a latch typically protects a group
of objects, a mutex protects a single object.
互斥对象(mutex)是一种阻止对象进入的低级机制当被并发访问时，内存不会老化或损坏流程。互斥锁类似于闩锁，但闩锁通常保护一个组对于对象，互斥锁保护单个对象。

* A mutex can reduce the possibility of contention. 互斥锁可以减少争用的可能性。
Because a latch protects multiple objects, it can become a bottleneck when
processes attempt to access any of these objects concurrently. By serializing access
to an individual object rather than a group, a mutex increases availability.
* A mutex consumes less memory than a latch. 互斥锁消耗的内存比闩锁少。
* When in shared mode, a mutex permits concurrent reference by multiple sessions. 当处于共享模式时，一个互斥锁允许多个会话并发引用

### Internal Locks 内部锁
Internal locks are higher-level, more complex mechanisms than latches and mutexes
and serve various purposes. 
内部锁是比锁存和互斥锁更高级、更复杂的机制有多种用途。

* Dictionary cache locks 字典缓存锁
These locks are of very short duration and are held on entries in dictionary caches
while the entries are being modified or used. They guarantee that statements being
parsed do not see inconsistent object definitions. Dictionary cache locks can be
shared or exclusive. Shared locks are released when the parse is complete, whereas
exclusive locks are released when the DDL operation is complete.
* File and log management locks 文件和日志管理锁
These locks protect various files. For example, an internal lock protects the control
file so that only one process at a time can change it. Another lock coordinates the
use and archiving of the online redo log files. Data files are locked to ensure that
multiple instances mount a database in shared mode or that one instance mounts
it in exclusive mode. Because file and log locks indicate the status of files, these
locks are necessarily held for a long time.
* Tablespace and undo segment locks 表空间锁和撤销段锁
These locks protect tablespaces and undo segments. For example, all instances
accessing a database must agree on whether a tablespace is online or offline. Undo
segments are locked so that only one database instance can write to a segment.
