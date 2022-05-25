# Concurrent Collections 线程集合类
下面这些线程集合类可以避免线程一致性错误。

**BlockingQueue** defines a first-in-first-out data structure that blocks or times out when you attempt to add to a full queue, or retrieve from an empty queue.
阻塞队列：一种先进先出的数据结构，搜索空队列或者在满队列的情况下插入元素会导致阻塞。

**ConcurrentMap** is a subinterface of java.util.Map that defines useful atomic operations. These operations remove or replace a key-value pair only if the key is present, or add a key-value pair only if the key is absent. Making these operations atomic helps avoid synchronization. The standard general-purpose implementation of ConcurrentMap is ConcurrentHashMap, which is a concurrent analog of HashMap.
ConcurrentMap是Map的一种并发实现，其中的元素增删改查都是原子的，比较有代表性的就是HashMap的并发版ConcurrentHashMap。

**ConcurrentNavigableMap** is a subinterface of ConcurrentMap that supports approximate matches. The standard general-purpose implementation of ConcurrentNavigableMap is ConcurrentSkipListMap, which is a concurrent analog of TreeMap.
ConcurrentNavigableMap是ConcurrentMap一个子接口，支持模糊匹配。实现这个接口的是TreeMap并发版ConcurrentSkipListMap。