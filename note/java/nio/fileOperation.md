# 文件IO操作
## StandardOpenOptions 当读取文件时的默认打开选项
```text 
WRITE – Opens the file for write access.
APPEND – Appends the new data to the end of the file. This option is used with the WRITE or CREATE options.
TRUNCATE_EXISTING – Truncates the file to zero bytes. This option is used with the WRITE option.
CREATE_NEW – Creates a new file and throws an exception if the file already exists.
CREATE – Opens the file if it exists or creates a new file if it does not.
DELETE_ON_CLOSE – Deletes the file when the stream is closed. This option is useful for temporary files.
SPARSE – Hints that a newly created file will be sparse. This advanced option is honored on some file systems, such as NTFS, where large files with data "gaps" can be stored in a more efficient manner where those empty gaps do not consume disk space.
SYNC – Keeps the file (both content and metadata) synchronized with the underlying storage device.
DSYNC – Keeps the file content synchronized with the underlying storage device.
```
## 小文件的常用方法
```java 
// （因为小文件不会占用太多内存，也不会导致io长时间的阻塞，所以使用全量的方式操作）
write(Path, byte[], OpenOption...)
write(Path, Iterable< extends CharSequence>, Charset, OpenOption...)
// 读取文件
Path file = ...;
byte[] fileArray;
fileArray = Files.readAllBytes(file);

// 写文件
Path file = ...;
byte[] buf = ...;
Files.write(file, buf);
```
## 文本文件使用的缓冲读写方法
`java.nio.file`包下的类支持通过回避一些导致读写瓶颈的层而将数据转移到内存的读写通道方式，从而突破读写的瓶颈。
```java 
 newBufferedReader(Path, Charset)
 newBufferedWriter(Path, Charset, OpenOption...)

Charset charset = Charset.forName("US-ASCII");
try (BufferedReader reader = Files.newBufferedReader(file, charset)) {
    String line = null;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException x) {
    System.err.format("IOException: %s%n", x);
}

Charset charset = Charset.forName("US-ASCII");
String s = ...;
try (BufferedWriter writer = Files.newBufferedWriter(file, charset)) {
    writer.write(s, 0, s.length());
} catch (IOException x) {
    System.err.format("IOException: %s%n", x);
}
```

## java.io 中使用的非缓冲读写方法
```java 
 newInputStream(Path, OpenOption...) 
 newOutputStream(Path, OpenOption...)


Path file = ...;
try (InputStream in = Files.newInputStream(file);
    BufferedReader reader =
      new BufferedReader(new InputStreamReader(in))) {
    String line = null;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException x) {
    System.err.println(x);
}

import static java.nio.file.StandardOpenOption.*;
import java.nio.file.*;
import java.io.*;

public class LogFileTest {

  public static void main(String[] args) {

    // Convert the string to a
    // byte array.
    String s = "Hello World! ";
    byte data[] = s.getBytes();
    Path p = Paths.get("./logfile.txt");

    try (OutputStream out = new BufferedOutputStream(
      Files.newOutputStream(p, CREATE, APPEND))) {
      out.write(data, 0, data.length);
    } catch (IOException x) {
      System.err.println(x);
    }
  }
}

```
## 通道读写的方法
读写流操作一次读取一个字符，通道读写一次读写一个缓冲区。
通道读写可以保持和更改通道的位置、截断通道中的文件以及查询已经连接的文件的大小。
通道读写可以指定通道的任意位置进行读写。
```java 
newByteChannel(Path, OpenOption...)
newByteChannel(Path, Set<? extends OpenOption>, FileAttribute<?>...)

// 通道读写默认打开读操作
// Defaults to READ
try (SeekableByteChannel sbc = Files.newByteChannel(file)) {
    ByteBuffer buf = ByteBuffer.allocate(10);

    // Read the bytes with the proper encoding for this platform.  If
    // you skip this step, you might see something that looks like
    // Chinese characters when you expect Latin-style characters.
    String encoding = System.getProperty("file.encoding");
    while (sbc.read(buf) > 0) {
        buf.rewind();
        System.out.print(Charset.forName(encoding).decode(buf));
        buf.flip();
    }
} catch (IOException x) {
    System.out.println("caught exception: " + x);
}

import static java.nio.file.StandardOpenOption.*;
import java.nio.*;
import java.nio.channels.*;
import java.nio.file.*;
import java.nio.file.attribute.*;
import java.io.*;
import java.util.*;

public class LogFilePermissionsTest {

  public static void main(String[] args) {
  
    // Create the set of options for appending to the file.
    Set<OpenOption> options = new HashSet<OpenOption>();
    options.add(APPEND);
    options.add(CREATE);

    // Create the custom permissions attribute.
    Set<PosixFilePermission> perms =
      PosixFilePermissions.fromString("rw-r-----");
    FileAttribute<Set<PosixFilePermission>> attr =
      PosixFilePermissions.asFileAttribute(perms);

    // Convert the string to a ByteBuffer.
    String s = "Hello World! ";
    byte data[] = s.getBytes();
    ByteBuffer bb = ByteBuffer.wrap(data);
    
    Path file = Paths.get("./permissions.log");

    try (SeekableByteChannel sbc =
      Files.newByteChannel(file, options, attr)) {
      sbc.write(bb);
    } catch (IOException x) {
      System.out.println("Exception thrown: " + x);
    }
  }
}


  String s = "I was here!\n";
        byte[] data = s.getBytes();
        ByteBuffer out = ByteBuffer.wrap(data);
        Path file = Paths.get("./permissions.log");

        ByteBuffer copy = ByteBuffer.allocate(12);

        try (FileChannel fc = (FileChannel.open(file, READ, WRITE))) {
            // Read the first 12
            // bytes of the file.
            int nread;
            do {
                nread = fc.read(copy);
            } while (nread != -1 && copy.hasRemaining());

            // Write "I was here!" at the beginning of the file.
            fc.position(0);
            while (out.hasRemaining()) {
                fc.write(out);
            }
            out.rewind();

            // Move to the end of the file.  Copy the first 12 bytes to
            // the end of the file.  Then write "I was here!" again.
            long length = fc.size();
            fc.position(length - 1);
            copy.flip();
            while (copy.hasRemaining()) {
                fc.write(copy);
            }
            while (out.hasRemaining()) {
                fc.write(out);
            }
        } catch (IOException x) {
            System.out.println("I/O Exception: " + x);
        }

```
## 创建文件以及临时文件的方法

```java 
createFile(Path, FileAttribute<?>)
createTempFile(Path, String, String, FileAttribute<?>)
createTempFile(String, String, FileAttribute<?>)

Path file = ...;
try {
    // Create the empty file with default permissions, etc.
    Files.createFile(file);
} catch (FileAlreadyExistsException x) {
    System.err.format("file named %s" +
        " already exists%n", file);
} catch (IOException x) {
    // Some other sort of failure, such as permissions.
    System.err.format("createFile error: %s%n", x);
}


try {
    Path tempFile = Files.createTempFile(null, ".myapp");
    System.out.format("The temporary file" +
        " has been created: %s%n", tempFile)
;
} catch (IOException x) {
    System.err.format("IOException: %s%n", x);
}
```
























