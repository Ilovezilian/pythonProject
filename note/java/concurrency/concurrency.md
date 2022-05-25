# 并发

## 死锁、饥饿、活锁

死锁`Deadlock`：

​	指两个以上的线程互相等待获取对方资源而导致一直阻塞下去的情况。你（线程）不能给你媳妇（线程）你的房子（资源）但是你要你媳妇的车子（资源），同样你媳妇不给你她的车子但是需要你的房子，此情景是为死锁。

> *Deadlock* describes a situation where two or more threads are blocked forever, waiting for each other. 

饥饿`Starvation`：

​	指线程一直获取不到需要的资源导致阻塞。家里三只小狗（线程）吃奶（资源），小的那只因为各种原因每次都吃不到奶，只能饿死，乃为饥饿。

> *Starvation* describes a situation where a thread is unable to gain regular access to shared resources and is unable to make progress.
>
> This happens when shared resources are made unavailable for long periods by "greedy" threads. For example, suppose an object provides a synchronized method that often takes a long time to return. If one thread invokes this method frequently, other threads that also need frequent synchronized access to the same object will often be blocked.

活锁 `Livelock`：

​	线程提示对方获得资源而导致都没有获得资源的情况。就是多个人（线程）吃菜（资源），一直相互客气请对方先吃，直到菜凉凉，定为活锁。

> A thread often acts in response to the action of another thread. 
>
> If the other thread's action is also a response to the action of another thread, then *livelock* may result. As with deadlock, livelocked threads are unable to make further progress. However, the threads are not blocked — they are simply too busy responding to each other to resume work. This is comparable to two people attempting to pass each other in a corridor: Alphonse moves to his left to let Gaston pass, while Gaston moves to his right to let Alphonse pass. Seeing that they are still blocking each other, Alphone moves to his right, while Gaston moves to his left. They're still blocking each other, so...



隐式锁`implicit locks` 

`synchronized`包含的代码段或者方法就是隐式锁

显式锁

1、支持`wait/notify`机制

2、获取锁失败可以取消获取

