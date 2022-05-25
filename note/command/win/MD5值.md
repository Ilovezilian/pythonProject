# 在Windows中查看文件的MD5值
Command Prompt（CMD）、Powershell、cmdler 均可。

```cmd 
certutil -hashfile 文件路径/文件名称 MD5
certutil -hashfile 文件路径/文件名称 SHA1
certutil -hashfile 文件路径/文件名称 SHA256
```

例如
```cmd 
certutil -hashfile /d/Downloads/ScheduleShiftListHandler.class
 MD5
MD5 的 D:/Downloads/ScheduleShiftListHandler.class 哈希:
93f8492e2c86ebaed8959bbfcd9b71d3
CertUtil: -hashfile 命令成功完成。
```
