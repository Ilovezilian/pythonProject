# git
## 基本操作
### 查看配置
``` git 
git config -l/--list
```
### 账号名邮箱
```git  
git config --global user.name "shuai pan"
git config --global user.email pandingrong0129@formail.com
```
### 寻求提示
* 查看帮助页面
```git 
git help config
git config -h
man git-<verb>
```
* 查找简单帮助提示
```git 
git config -h/-help
```
### 查看状态
```git 
git status -s
```
### 查看不同
```git 
// 查看未暂存（staged）的变更 Changes in the working tree not yet staged for the next commit.
git diff 
// 查看已经暂存（staged）未提交(commit)的变更 Changes between the index and your last commit; what you would be committing if you run "git commit" without "-a" option.
git diff --cached/--staged
// 查看所有未提交(commit)变更 Changes in the working tree since your last commit; what you would be committing if you run "git commit -a"

```

### 撤回修改未暂存 Unstaged => Unmodified
```git 
git checkout -- <file>
```

### 添加 Untracked、Unstaged => Staged
``` git
git add path/*
```

### 撤回暂存 Staged => Unstaged
```git 
git reset HEAD <file>
```

### 提交 Staged => Unmodified
```git 
// 提交
git commit -m "description"
// 修正提交
git commit --amend
// 多次-修正提交
git rebase continue
// 反转提交记录
git rebase i HEAD~3

```

### 删除
#### 删除本地和暂存(Staged)的文件
```git 
git rm <file>
```
####  删除暂存(Staged)的文件，保留本地文件
```git 
git rm --cached <file>

```

## 日志
### 查看日志
```git 
// 查看当前分录的历史日志
git log 
// 查看近期（几个月）历史操作日志
git reflog
```

## 仓库操作
### 初始化
``` git 
git init
git clone https://github.com:Ilovezilian/job.git projectName
```

## 远程
### 查看远程仓库
```git 
git remote
git remote -v 
```
### 添加远程仓库
```git 
git remote add <shortname> <url>
```
### 删除远程仓库
```git 
git remote remove/rm <remote>
```
### 获取远程仓库
```git 
git fetch <remote>
git pull <remote> <branch>
```
### 推送远程仓库
```git 
git push <remote> <branch>
```

### 缩写
```git 
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

git config --global alias.unstage 'reset HEAD --'

git config --global alias.last 'log -1 HEAD'

git config --global alias.visual '!gitk'

```

## 分支
### 查看分支
```git
// 查看分支信息
git branch -v
// 查看合并过的分支
git branch --merged
// 查看未合并分支
git branch --no-merged <commit>
```
### 添加分支
```git 
git checkout <branch>
git branch <branch>
```
### 合并分支
```git 
git merge --no-ff <branch>
```
### 冲突解决工具
```git 
git mergetool
// 查看支持的工具
git mergetool --tool-help 
// 使用指定的工具
git meregetool -t/--tool <tool>
```

## 工具
### 储存
```git 
// 储存列表
git stash list
// 储存
git stash 
git stash save
git stash push
// 放出
git stash pop
git stash apply 
git stash apply stash@{2}
// 删除
git stash drop stash@{0}
```
### 清空
```git 
// 删除所有新增未跟踪（untracked）并且不被忽略（ignore）的文件
git clean
// 预演 删除所有新增未跟踪的文件（untracked）-不会删除
git clean -d -n
// 删除所有新增未跟踪的文件（untracked）
git clean -f -d


```

