@echo off
:: https://www.cnblogs.com/yang-hao/p/6003923.html
:: 1) OPTION关键字详解:
::　　eol=c：指一个行注释字符的结尾(就一个)。例如：eol=; --忽略以分号打头的那些行;
::　　skip=n：指在文件开始时忽略的行数。例如：skip=2 --忽略2行；
::　 delims=xxx：指分隔符集。这个替换了空格和跳格键的默认分隔符集。例如：[delims=, ] --指定用逗号，空格对字符串进行分隔。
　　tokens=x,y,m-n：指每行的哪一个符号被传递到每个迭代的 for 本身。这会导致额外变量名称的分配。m-n格式为一个范围。通过 nth 符号指定 mth。如果符号字符串中的最后一个字符是星号，那么额外的变量将在最后一个符号解析之后分配并接受行的保留文本。例如：tokens=2,3* --将每行中的第二个和第三个符号传递给 for 程序体；tokens=2,3* ... i% --将会把取到的第二个字符串赋给i%,第三个赋给j%,剩下的赋给k%。
for /f "tokens=*" %%a in ('jps ')  do echo %%a
echo.

:: 最后还有skip合eol，这俩个简单，skip就是要忽略文件的前多少行，而eol用来指定当一行以什么符号开始时，就忽略它。
:: 对以通配符*，就是把这一行全部或者这一行的剩余部分当作一个元素了。
for /f "tokens=* delims= " %%i in (D:\git\job\src\main\resources\command\a.txt) do echo %%i
echo.

:: 如果要显示第二列和第三列，则换成tokens=2,3或tokens=2-3,如果还有更多的则为：tokens=2-10之类的。
:: 怎么多出一个%%j？
:: 这是因为你的tokens后面要取每一行的两列，用%%i来替换第二列，用%%j来替换第三列。
:: 并且必须是按照英文字母顺序排列的，%%j不能换成%%k，因为i后面是j
for /f "tokens=2,3 delims= " %%i in (D:\git\job\src\main\resources\command\a.txt) do echo %%i %%j
echo.
:: 第1行第2列 第1行第3列
:: 第2行第2列 第2行第3列
:: 第3行第2列 第3行第3列

for /f "tokens=2 delims= " %%i in (D:\git\job\src\main\resources\command\a.txt) do echo %%i
echo.
:: 第1行第2列
:: 第2行第2列
:: 第3行第2列

for /f "delims= " %%i in (D:\git\job\src\main\resources\command\a.txt) do echo %%i
echo.
:: 第1行第1列
:: 第2行第1列
:: 第3行第1列

:: 这个会显示a.txt里面的内容，因为/f的作用，会读出a.txt中
for /f %%a in (D:\git\job\src\main\resources\command\a.txt) do echo %%a
echo.
:: 第1行第1列
:: 第2行第1列
:: 第3行第1列

::而这个只会显示a.txt这个名字，并不会读取其中的内容。
for %%i in (D:\git\job\src\main\resources\command\a.txt) do echo %%i
echo.

:: 迭代数值范围:系统帮助的格式:for /L %% Variable in (Start#,Step#,End#) do Command
for /l %%a in (1,1,4) do (
echo hehe %%a
)
echo.
:: hehe 1
:: hehe 2
:: hehe 3
:: hehe 4

for /d %%i in (*) do @echo %%i
:: for /r d:/Downloads %%i in (*.exe) do @echo %%i
echo.
