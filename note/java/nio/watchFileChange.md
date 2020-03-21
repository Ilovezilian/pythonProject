# 监控文件夹以及文件变更
## 总体步骤
* Create a WatchService "watcher" for the file system.
* For each directory that you want monitored, register it with the watcher. When registering a directory, you specify the type of events for which you want notification. You receive a WatchKey instance for each directory that you register.
* Implement an infinite loop to wait for incoming events. When an event occurs, the key is signaled and placed into the watcher's queue.
* Retrieve the key from the watcher's queue. You can obtain the file name from the key.
* Retrieve each pending event for the key (there might be multiple events) and process as needed.
* Reset the key, and resume waiting for events.
* Close the service: The watch service exits when either the thread exits or when it is closed (by invoking its closed method).

## 监控处理步骤
1. Get a watch key. Three methods are provided:
    poll – Returns a queued key, if available. Returns immediately with a null value, if unavailable.
    poll(long, TimeUnit) – Returns a queued key, if one is available. If a queued key is not immediately available, the program waits until the specified time. The TimeUnit argument determines whether the specified time is nanoseconds, milliseconds, or some other unit of time.
    take – Returns a queued key. If no queued key is available, this method waits.
2. Process the pending events for the key. You fetch the List of WatchEventsfrom the pollEvents method.
3. Retrieve the type of event by using the kind method. No matter what events the key has registered for, it is possible to receive an OVERFLOW event. You can choose to handle the overflow or ignore it, but you should test for it.
4. Retrieve the file name associated with the event. The file name is stored as the context of the event, so the context method is used to retrieve it.
5. After the events for the key have been processed, you need to put the key back into a ready state by invoking reset. If this method returns false, the key is no longer valid and the loop can exit. This step is very **important**. If you fail to invoke reset, this key will not receive any further events.

监听键的状态：
* Ready indicates that the key is ready to accept events. When first created, a key is in the ready state.
* Signaled indicates that one or more events are queued. Once the key has been signaled, it is no longer in the ready state until the reset method is invoked.
* Invalid indicates that the key is no longer active. This state happens when one of the following events occurs:
    * The process explicitly cancels the key by using the cancel method.
    * The directory becomes inaccessible.
    * The watch service is closed.


## 使用或者不使用情况
使用的场景很多，
不使用的场景是看文件系统是否支持。不支持的话，监听线程就会一直无限阻塞在哪里。