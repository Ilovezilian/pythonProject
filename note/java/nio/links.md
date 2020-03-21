# 符号链接
## 前言 恶补一下windows的链接

> vista及以上系统的mklink命令可以创建文件夹的链接（感觉像是文件夹的映射）。因为是从底层实现文件夹链接，所以这个链接是对应用程序透明的。
> 这样c盘下面就会多出一个带快捷方式图标的文件夹，全称就是"C:\Program Files"，双击进去其实就转到了D:\Program Files。

```
mklink /j "C:\Program Files" "D:\Program Files"
```
> 1，上面建立的链接属于软链接(/j)，还有符号链接(/d)和文件的硬链接(/h)。
> 
> 符号链接和软链接大致相同，区别在于，软链接是绝对路径链接，而符号链接允许相对路径的链接。
> 
> 比如，分别创建c:\data\tmp的符号链接c:\1和软链接c:\2，那么c:\1指向的就是同级文件夹下的data文件夹下的子文件夹tmp，而c:\2指向的是c:\data\tmp这样的绝对路径。影响就是，如果把c:\1和c:\2这两个文件夹移动到d盘，那d:\1的链接就失效了，而d:\2仍然有效。
> 
> 文件的硬链接是对文件创建的链接，比如对c:\data\1.txt创建链接c:\data\2.txt，那么这两个文件就是同一个文件的两个等价别名了，相当于是指向同一个硬盘存储空间的两个指针，删除其中任何一个都不影响另一个文件。但是限制就是这种链接不能跨分区。
> 
> 2，软链接和符号链接不能跨磁盘。
> 
> 3，这个功能必须是在ntfs文件系统上才能使用。

[以上参考](https://www.cnblogs.com/plusium/archive/2010/03/17/1688511.html)

## 创建软链接
```java 
   @SneakyThrows
    @Test
    public void createSymbolicLink() {
        Path newLink = Paths.get(Constants.BASE_DIRECTORY + "/heihei");
        Path targetLink = Paths.get(Constants.BASE_DIRECTORY + "/readme.md");
        Files.createSymbolicLink(newLink, targetLink);
    }
```
## 创建硬链接
```java 
  @SneakyThrows
    @Test
    public void createHardLink() {
        Path newLink = Paths.get(Constants.BASE_DIRECTORY + "/heihei.md");
        Path targetLink = Paths.get(Constants.BASE_DIRECTORY + "/readme.md");
        Files.createLink(newLink, targetLink);
    }
```
## 检测是否为软连接
```java 
  @SneakyThrows
    @Test
    public void detectSymbolicLink() {
        Path path = Paths.get(Constants.BASE_DIRECTORY);
        try (final DirectoryStream<Path> paths = Files.newDirectoryStream(path, "*.md")) {
            for (Path file : paths) {
                System.out.print("file = " + file);
                System.out.println(Files.isSymbolicLink(file) ? "is symbolic link" : "");
            }
        }
    }
```
## 读取软连接路径
```java 
Path link = ...;
try {
    System.out.format("Target of link" +
        " '%s' is '%s'%n", link,
        Files.readSymbolicLink(link));
} catch (IOException x) {
    System.err.println(x);
}
```

