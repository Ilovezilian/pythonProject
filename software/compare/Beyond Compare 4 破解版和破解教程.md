> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/testunit/article/details/90408371)

## [Beyond Compare 4](Beyond Compare 4.md)  破解版和破解教程
[[Beyond Compare 4]]
[Beyond Compare](https://so.csdn.net/so/search?q=Compare&spm=1001.2101.3001.7020) 用于文件比较还是蛮好的选择，特别是我们程序袁用于比较两个项目的时候，最初使用的是 Beyond Compare3 一直用着挺好的，几年前更新了版本 4，用着用着就提示试用期 30 天已过期，于是我尝试如下步骤：
1.       网上下载个 Beyond Compare3，反正 3 也好用没必要非得升到 4，我上网搜了一下，无奈发现 3 的链接很少，即使有几个是 3 的链接，下载下来还是版本 4，还是要注册。

2.       网上搜索 Beyond Compare4 绿色破解版，既然 3 不能用了就下载 4 吧，用最新的也挺好，只要是破解版，链接搜索到一大堆，有的是压根还是试用版，有的提供注册码，但注册码已经过期了，有的提供注册机，注册机点了半天没反应

3.       思来想去，尽然网上资源有限就在即破除这个限制吧，你不是检测已经试用 30 天了吗，老子卸载重装可以了吧，试用 30 天再重装，麻烦事就麻烦事一点，没办法，于是我卸载了重装，还是提示试用过期，看来这 B 留了个心眼，卸载时候没有完全卸载干净，那老子帮你卸载干净行不？我拿起 everthing, 把所有关于 Beyond Compare 的文件和文件夹全都删掉，又在注册表里面搜索了一通，也把所有关于 Beyond Compare 的项全部删除掉，启动了一下还是他妈提示过期。汗。。。

4.       这他妈不是官逼民反吗？老子寻思，打开 OD, 一边安装 IDA, 好几年不弄这些了，逼老子，没办法。把 Beyond Compare 拖入到 OD, 看了下入口汇编代码，应该是没有加壳，这就好办多了，结下了就从弹那个对话框 “你的 30 天评估期已经结束” 下手。

![](http://www.pianshen.com/images/313/f9a4e0d32d3975c1703f57e74d5a5189.png)

搜索这串字符串，发现没搜索到，看来程序还是做了一定防护的。隐藏了字符串。

F9 运行程序到弹出对话框，点击暂停按钮，再点击工具栏的字母 K。出现如下对话框，

![](http://www.pianshen.com/images/780/89b8106f2c2196b8bc04d06ed3768d9c.png)

我们看到这个对话框是有 API-user32.MessageBoxExA 团出来的，我们就在这个 API 上下断点，

![](http://www.pianshen.com/images/129/0d095706eb34b6ef0c0bb445ee61a0f9.png)

如图，工具栏里面有菜单可以对这个 API 下断点了，也可在下面的命令框里面输入 bp MessageBoxExA。接着重新加载一下这个程序，F9 运行，我们看到到断点那里停了下来，F8 单步运行知道运行到程序领空（现在是在系统领空）。如下图：

![](http://www.pianshen.com/images/540/420179b96178dbebc078d395e2141a84.png)

CTRL+A 分析一下代码：

![](http://www.pianshen.com/images/156/942f6b7f13757ff7df6e9662834f324c.png)

我们简单的看下这段代码，有个条件跳转, 下面有个弹框 API + 打开浏览器接着 ExitProcess。看下这个跳转正好跳过这段代码，他这个逻辑相当清晰了：

```
验证结果=验证程序（）
 
If（验证结果==失败）
 
{
 
弹框+跳转付费网站+退出程序
 
}
 
继续执行功能，
```

分析到这里是不是就很好办了，改这个跳转指令直接跳过就行了，jp->jmp。还判断个球啊。

改过之后保存文件，替换原来的。

![](http://www.pianshen.com/images/87/81e5833a2f90f637dc1bb146a65f9aef.png)

看到了久违的文件比较工具。

哎，我说你这个公司也真是，这么好的程序你非得收费，收费你又不好好做收费程序，你这不是欺负软柿子吗？

原文地址：[http://www.pianshen.com/article/341259460/](http://www.pianshen.com/article/341259460/)