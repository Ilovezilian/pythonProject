# 文件夹操作

## 查看文件系统的所有根目录
```java 
  for (Path path : FileSystems.getDefault().getRootDirectories()) {
            System.out.println("path = " + path);
            /**
             * path = C:\
             * path = D:\
             * path = E:\
             */
        }
```
## 创建目录
```java 
 createDirectory(Path, FileAttribute<?>) // 创建单个目录，目录存在会报错
 createDirectories(Path, FileAttribute<?>) // 创建多个目录，不存在就创建，已存在也不会报错

Path dir = ...;
Files.createDirectory(path);

Set<PosixFilePermission> perms =
    PosixFilePermissions.fromString("rwxr-x---");
FileAttribute<Set<PosixFilePermission>> attr =
    PosixFilePermissions.asFileAttribute(perms);
Files.createDirectory(file, attr);

```

## 创建临时目录
```java 
createTempDirectory(Path, String, FileAttribute<?>...)
createTempDirectory(String, FileAttribute<?>...)

```

## 列出目录的内容
```java 
 newDirectoryStream(Path)

Path dir = ...;
try (DirectoryStream<Path> stream = Files.newDirectoryStream(dir)) {
    for (Path file: stream) {
        System.out.println(file.getFileName());
    }
} catch (IOException | DirectoryIteratorException x) {
    // IOException can never be thrown by the iteration.
    // In this snippet, it can only be thrown by newDirectoryStream.
    System.err.println(x);
}
```
## 用Glob表达式过滤目录列表
```java 
Path dir = ...;
try (DirectoryStream<Path> stream =
     Files.newDirectoryStream(dir, "*nicaye*.{java,class,jar}")) {
    for (Path entry: stream) {
        System.out.println(entry.getFileName());
    }
} catch (IOException x) {
    // IOException can never be thrown by the iteration.
    // In this snippet, it can // only be thrown by newDirectoryStream.
    System.err.println(x);
}

```
## 使用自定义Filter过滤目录表
```java 
 DirectoryStream.Filter<Path> filter = file -> (Files.size(file) > 5120L); // 大于 5KB的文件
 try (final DirectoryStream<Path> paths = Files.newDirectoryStream(dir, filter)) {
    for (Path path : paths) {
        System.out.println("path = " + path.toString() + " size = " + Files.size(path));
    }
 }
```






















