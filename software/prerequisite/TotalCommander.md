# Total Commander (TC)
## 来历
从[善用佳软](https://xbeta.info/studytc/index.htm)中，无意间看到并且适用的。

## 原因（摘抄的）
1. Total Commander 本身是一个非常优秀的软件，值得软件爱好者关注。
2. 了解 Total Commander 的发展历史、功能定位、开发方向，可以让用户建立正确的软件价值观，从而有助于对其他软件更深刻（而不是肤浅的）评价和认识。
3. Total Commander 是一个会显著提高文件操作效率的工具，而文件操作是应用计算机最基本的功夫，也是伴随一生的操作。因此花一点时间学习，而会受益一世。
4. TC 的入门有一定难度，掌握 TC 后，会让自己在软件应用方面的能力和悟性上一个台阶。

## 快捷键
快捷键 | 功能
--- | ---
ctrl+\ | 可一步跳转到根目录
ctrl+-> | 把左边映射到右边
ctrl+<- | 把右边映射到左边
ctrl+u | 交换窗口
alt+F5 | 压缩到对面窗口
ALT+SHIFT+F5 | 移动到压缩文件中
ctrl+alt+F5 | 压缩到当前目录
alt+F6/alt+F9 | 解压缩
F4 | 编辑文件
shift+F4 | 新建文件
F5 | 从当前窗口 复制 到对面窗口
shift+F5 | 复制文件到当前窗口
F6 | 从当前窗口 移动 到对面窗口
shift+F6 | 重命名
F7 | 创建文件夹
alt+F7 | 搜索文件
ALT+SHIFT+F7 | 用单独线程搜索文件
alt+F0 | 打开文件夹树并定位到当前位置
CTRL+PgDn | 进入下一层目录（和enter大致相同，也可以进入zip、exe文件内）
CTRL+F8 | 当前窗口设置文件夹树
CTRL+shift+F8 | 展示各出窗口文件夹树，不显示、显示一个、显示两个
space/insert | 选择
ctrl+f | 打开ftp链接
ctrl+shift+f | 取消ftp链接
ctrl+l | 计算文件大小
ctrl+m | 批量改名
ctrl+r | 刷新
ctrl+s | 激活或禁用过滤


## 配置
安装目录：的 wincmd.ini
``` config

[Configuration]

StartupScreen=0


InstallDir=d:\totalcmd
languageini=wcmd_chn.lng
Mainmenu=wcmd_chn.mnu
UseNewDefFont=0
firstmnu=2672
FirstTime=0
test=6
BreadcrumbDelayButton=-250
ShowHiddenSystem=1
UseLongNames=1
Small83Names=0
OldStyleTree=0
autotreechange=0
DirBrackets=0
ShowParentDirInRoot=1
SortDirsByName=0
Tips=3
FileTipWindows=1
Win32TipWindows=0
SortUpper=0
IconOverlays=0
IconsSpecialFolders=3
Showicons=2
ShowEXEandLNKicons=0
IconsInMenus=16
IconsOnNet=1
ShowCentury=0
Aligned extension=0
SizeStyle=1
SizeFooter=3
DirTabOptions=1848
DirTabLimit=32
onlyonce=1
TrayIcon=1
UseRightButton=0
Savepath=1
Savepanels=0
MarkDirectories=1
AlwaysToRoot=1
SingleClickStart=0
RenameSelOnlyName=1
SaveCommands=1
SaveHistory=1
CountSpace=1
CountMarked=1
1hourdif=0
CopyComments=2
CommentPreferredFormat=3
IconClickSelection=1
Viewer=E:\download\softwareOfWindows\gvim74\gVimPortable_7.4\vim74\gvim.exe "%1"
Editor=E:\download\softwareOfWindows\gvim74\gVimPortable_7.4\vim74\gvim.exe "%1"
Viewertype=1
ExplorerForCopy=0
CopyHugeBlockSize=10240
CopyHugeBlockSizeOther=64
SamePartitions=DE
CopyDefaultMethod=0
Win95Delete=1
UseTrash=1
noreread=\
WatchDirs=0
AltSearch=3
QuickSearchMatchBeginning=0
QuickSearchExactMatch=1
ThumbsLocation=
ThumbsCopyDel=0
ThumbsCustomFieldsEnabled=0
ThumbWidthNoCache=96
ThumbHeightNoCache=96
ThumbOptions=10
ThumbExplTypes=*.* | *.htm *.html
ThumbPlgTypes=*.*
ThumbIrfXnTypes=*.*
ThumbTxtTypes=*.txt *.ini
LogFile=%TEMP%\totalcmd.log
LogOptions=7181
LogRotateLimit=1000
LogKeepCount=3
FirstTimeZIP=0
SoundDelay=10
LastSearchOptions=32
UseEverything=0
FirstTimeUnpack=0
SeparateTree=0
PanelsVertical=0
CompareCaseSensitive=0
CompareIgnoreRepSpace=1
CompareIgnoreRepeatedLines=1
CompareVertical=0
QuickSearchAutoFilter=1
UseRubberBandSelection=1
[Buttonbar]
IconDll_default.bar=
IconDll_vertical.bar=
[FileSystemPlugins64]
$checksum$=3014672
[Layout]
ButtonBar=0
ButtonBarVertical=1
DriveBar1=0
DriveBar2=0
DriveBarFlat=1
InterfaceFlat=1
DriveCombo=0
DirectoryTabs=1
XPthemeBg=0
CurDir=1
TabHeader=1
StatusBar=1
CmdLine=0
KeyButtons=0
HistoryHotlistButtons=1
BreadCrumbBar=1
[1366x768 (8x16)]
FontSize=11
FontName=Tahoma
FontSizeWindow=8
FontNameWindow=Tahoma
FontWeight=400
FontWeightWindow=400
FontNameDialog=Tahoma
Tabstops=178,182,244,-1,550,98
FontSizeDialog=11
SearchX=412
SearchY=252
SearchDX=580
SearchDY=163
SearchMax=0
MenuChangeX=375
MenuChangeY=250
MenuChangeDX=476
MenuChangeDY=354
MenuChangeMax=0
PluginSelX=404
PluginSelY=273
PluginSelDX=393
PluginSelDY=410
PluginSelMax=0
CustColumnX=185
CustColumnY=22
CustColumnDX=968
CustColumnDY=726
CustColumnMax=0
TreeDlgX=480
TreeDlgY=207
TreeDlgDX=421
TreeDlgDY=393
TreeDlgMax=0
ConnectX=261
ConnectY=201
ConnectDX=497
ConnectDY=381
ConnectMax=0
maximized=0
x=102
y=50
dx=1100
dy=668
Divider=500
DividerQuickView=500
DividerComments=500
CompareX=115
CompareY=144
CompareDX=974
CompareDY=459
CompareMax=1
CompareDivider=500
CmdSelX=22
CmdSelY=29
CmdSelDX=653
CmdSelDY=410
CmdSelMax=0
CompFontName=Courier New
Compfontsize=16
CompCharSet=134
CompFontStyle=400
RenameX=331
RenameY=148
RenameDX=720
RenameDY=510
RenameMax=0
RenameTabs=115,145,345,405,525
[AllResolutions]
FontSize=11
FontName=Tahoma
FontSizeWindow=8
FontNameWindow=Tahoma
FontWeight=400
FontWeightWindow=400
FontNameDialog=Tahoma
FontSizeDialog=11
[Tabstops]
0=178
1=182
3=244
4=-1
6=550
5=98
AdjustWidth=1
[Packer]
ZIPlikeDirectory=1
InternalUnarj=0
ARJlongnames=0
InternalUnlzh=0
InternalUnrar=0
InternalUnace=0
LinuxCompatible=0
ARJ=""C:\Program Files\7-Zip\7zFM.exe""
LHA=""C:\Program Files\7-Zip\7zFM.exe""
RAR=""C:\Program Files\7-Zip\7zFM.exe""
UC2=""C:\Program Files\7-Zip\7zFM.exe""
ACE=""C:\Program Files\7-Zip\7zFM.exe""
InternalZip=0
InternalUnzip=0
zipnt=0
ZIP=C:\Program Files\7-Zip\7zFM.exe
UnZIP=""C:\Program Files\7-Zip\7zFM.exe""
InternalZipRate=9
Zip83Name=0
ZipSetDateToNewest=1
nodelete=0
OpenPartial=0
[Confirmation]
deleteDirs=1
OverwriteFiles=1
OverwriteReadonly=0
OverwriteHidSys=0
MouseActions=0
[ContentPlugins64]
$checksum$=3014672
[SearchName]
0=wincmd.ini
[SearchIn]
0=d:\totalcmd
[ListerPlugins64]
$checksum$=3014672
[CustomFields]
AutoLoad=0
[Selection]
0=*.html *.htm *.jsp *xhtml
1=*.bmp *.gif *.jpg
[left]
userspec=*.bmp *.gif *.jpg
path=d:\Downloads\
ViewMode=10001
activepanelcolor=-1
activepanelcolor2=-1
ShowAllDetails=1
SpecialView=0
show=1
sortorder=0
negative Sortorder=0
[ViewModes]
0_name=<默认色>
0_icon=
0_options=-1|-1|0||-1|-1|-1
[searches]
2DayBefore_SearchFor=
2DayBefore_SearchIn=
2DayBefore_SearchText=
2DayBefore_SearchFlags=0|002002000020|||2|1|||||0000|||
1WeekBefore_SearchFor=
1WeekBefore_SearchIn=
1WeekBefore_SearchText=
1WeekBefore_SearchFlags=0|002002000020|||7|1|||||0000|||
[Colors]
ColorFilter1=>2DayBefore
ColorFilter1Color=255
ColorFilter2=>1WeekBefore
ColorFilter2Color=16711680
[right]
path=e:\download\chrome\pt\PT149474 850sp1\Server\server\lib\addon\attendmanage\lib\
ViewMode=10001
activepanelcolor=-1
activepanelcolor2=-1
ShowAllDetails=1
SpecialView=0
show=1
sortorder=0
negative Sortorder=0
userspec=*.html *.htm *.jsp *xhtml
[Command line history]
0=dir
[MkDirHistory]
[SearchText]
[RenameTemplates]
0=[N]
[1440x900 (8x16)]
MenuChangeX=375
MenuChangeY=250
MenuChangeDX=476
MenuChangeDY=354
MenuChangeMax=0
[1920x1080 (8x16)]
MenuChangeX=375
MenuChangeY=250
MenuChangeDX=476
MenuChangeDY=354
MenuChangeMax=0
CompFontName=Courier New
Compfontsize=16
CompCharSet=134
CompFontStyle=400
CompareX=306
CompareY=245
CompareDX=974
CompareDY=459
CompareMax=1
CompareDivider=500
ConnectX=261
ConnectY=201
ConnectDX=497
ConnectDY=381
ConnectMax=0
RenameX=608
RenameY=304
RenameDX=720
RenameDY=510
RenameMax=0
RenameTabs=115,145,345,405,525
[DirMenu]
menu1=&1 Documents
cmd1=cd d:\Documents
menu2=&2 Downloads
cmd2=cd d:\Downloads
menu4=&4 git
cmd4=cd d:\git
menu5=&5 BaiduYunDownload
cmd5=cd d:\BaiduYunDownload
menu8=&tt
cmd8=cd c:\tt
[RenameSearchFind]
0=庄
[RenameSearchReplace]
0=桩
[RightHistory]
[LeftHistory]
```