# 遇到的问题
## 数据库
### 链接数据库：
   在编写链接数据库的时候：to8to/dsp_ps_gdm/db/gdm_mysql.py出现问题
   文件名 为mysql.py，然后内容和现在是一样的。然后老是编译不过。
   ``` 
   C:\Users\SHUAI.PAN\AppData\Local\Programs\Python\Python37-32\python.exe "C:\Program Files\JetBrains\PyCharm 2018.2.4\helpers\pydev\pydevd.py" --multiproc --qt-support=auto --client 127.0.0.1 --port 57893 --file D:/git/pythonProject/to8to/dsp_ps_gdm/db/mysql.py
pydev debugger: process 10160 is connecting

Connected to pydev debugger (build 182.4505.26)
Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm 2018.2.4\helpers\pydev\pydevd.py", line 1664, in <module>
    main()
  File "C:\Program Files\JetBrains\PyCharm 2018.2.4\helpers\pydev\pydevd.py", line 1658, in main
    globals = debugger.run(setup['file'], None, None, is_module)
  File "C:\Program Files\JetBrains\PyCharm 2018.2.4\helpers\pydev\pydevd.py", line 1068, in run
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "C:\Program Files\JetBrains\PyCharm 2018.2.4\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
  File "D:/git/pythonProject/to8to/dsp_ps_gdm/db/mysql.py", line 1, in <module>
    import mysql.connector
  File "D:\git\pythonProject\to8to\dsp_ps_gdm\db\mysql.py", line 1, in <module>
    import mysql.connector
ModuleNotFoundError: No module named 'mysql.connector'; 'mysql' is not a package

Process finished with exit code 1
```
一直找，甚至还对比过路径，偶然才注意到   mysql.py文件里面引用mysql.connector 肯定优先引用自身。
然后文件名一改，就摆平问题。气死了。
   

