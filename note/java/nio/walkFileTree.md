# 遍历文件树
## 实现 FileVisitor 接口或者继承 SimpleFileVisitor 类
有下面几个接口需要注意，SimpleFileVisitor实现了要使用继承即可。复写的方法有：
preVisitDirectory – 在文件被访问之前调用的方法
postVisitDirectory – 在目录下所有的文件被访问完之后调用的方法，若访问文件时报错，方法不会被调用。
visitFile – 文件被访问时调用的方法
visitFileFailed – 文件访问报错后调用的方法

控制流程的 FileVisitResult 值：
CONTINUE – 遍历流程继续访问
TERMINATE – 无论流程跑到哪里，立即结束遍历
SKIP_SUBTREE – 遍历流程跳过指定的文件目录及其子目录
SKIP_SIBLINGS – 遍历流程跳过遍历指定目录及其同级目录

下面实现的类也可以作为静态内部类实现
```java 
public class PrintFiles extends SimpleFileVisitor<Path> {

    // Print information about each type of file.
    @Override
    public FileVisitResult visitFile(Path file, BasicFileAttributes attr) {
        if (attr.isSymbolicLink()) {
            System.out.format("Symbolic link: %s ", file);
        } else if (attr.isRegularFile()) {
            System.out.format("Regular file: %s ", file);
        } else {
            System.out.format("Other: %s ", file);
        }

        System.out.println("(" + ByteUnitEnum.getHumanSpace(attr.size()) + ")");
        return CONTINUE;
    }

    // Print each directory visited.
    @Override
    public FileVisitResult postVisitDirectory(Path dir, IOException exc) {
        System.out.format("Directory: %s%n", dir);
        return CONTINUE;
    }

    // If there is some error accessing the file, let the user know.
    // If you don't override this method and an error occurs, an IOException is thrown.
    @Override
    public FileVisitResult visitFileFailed(Path file, IOException exc) {
        System.err.println(exc);
        return CONTINUE;
    }
}
```
## 遍历方法
> tip：为了产生报错，尝试了禁用文件的各个用户组的各种权限，但是文件还是照常输出，没有任何异常；
还想要通过程序访问来占用文件的锁，从而导致报错，but并没有什么卵用；
最后通过禁用文件夹的方式才得到没有权限访问的文件，突然觉得对windows的权限还木有这么熟悉。
还是需要好好学习。

遍历方法是深度优先遍历
```java 
walkFileTree(Path, FileVisitor)
walkFileTree(Path, Set<FileVisitOption>, int, FileVisitor)
```
```text 
Regular file: d:\tmp\bar\foo\readme.md (3K)
Regular file: d:\tmp\bar\foo\test\readme.md (3K)
Directory: d:\tmp\bar\foo\test
Directory: d:\tmp\bar\foo
Regular file: d:\tmp\bar\readme.md (3K)
Directory: d:\tmp\bar
Regular file: d:\tmp\heihei.md (3K)
Regular file: d:\tmp\heihei.md - 快捷方式.lnk (565B)
java.nio.file.AccessDeniedException: d:\tmp\forbidDir // 终于出现的错误，人生如此艰难
Regular file: d:\tmp\readme.md (3K)
Regular file: d:\tmp\temp.xlsx (9K)
```