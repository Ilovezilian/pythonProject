### 版本

```text
eas 850: 
PT129457
PT134017
```

### 线程

```txt
**相关工具路径：eas\Server\server\deploy\eas.ear\cp_web.war\tools**

http://localhost:6888/easportal/tools/getclassurl.jsp?className=com.kingdee.eas.hr.ats.ScheduleShift
> 这个工具只适用于后端(shr-ats, shr-atscontrl)Java类，前端(attendmanage, attendContrl)Java类不适用 -- 这也坑
http://localhost:6888/easportal/tools/getclasspath.jsp
> 参考楼上
http://localhost:6888/easportal/tools/threaddump.jsp
http://localhost:6888/easportal/tools/threaddump_mi.jsp
```

### 数据库连接

```txt
http://59.57.246.50/easportal/tools/apusicjdbctrace.jsp
```
eas数据库查询过程 打开 sql 办法 

1. 流程引擎日志：直接在搜索框查询"流程引擎"

2. 启动sql分析器：ctrl+shift+q
3. uuid可以通过id查询对应的表

### 客户代码路径

```txt
前端代码
\eas\server\deploy\easweb.ear\shr_web.war
后端代码
eas\server\lib\addon\attendmanage\lib\attendmanage.jar
```

### 获取日志
#### 浏览器
```txt
url日志工具
    /shr/dynamic.do?uipk=atsDev&debug=true&inFrame=true&initialed=true
    ip:port:6888/shr/ces.jsp
平台工具
    /shr/appData.do?method=getApplicationLog&instance=server1&needBreak=true&logFile=apusic.log.0
    /shr/appData.do?method=getApplicationLog&instance=server1&needBreak=true&logFile=KSqlD.V60SP1.log
```
#### 服务器日志文件

```txt
对应实例下的log文件 w:\eas\Server\server\profiles\server1\logs\

日志密码：现在8.6下载的日志解压需要密码，密码为：kdshr+年月日（全称）
```


### web配置环境模式（建议开发模式）
```txt
开发在开发模式，为默认页面配置；产品配置在产品（拓展）模式，拓展模式优先级高于开发模式配置的页面。
http://127.0.0.1:6888/shr/dynamic.do?uipk=tools.dev
功能的路径来自自行查找：w:\eas\Server\server\deploy\eas.ear\cp_web.war\tools\*jsp
```
