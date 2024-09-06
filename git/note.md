# git 备忘

*2024-3-23*

- Git Reference: <https://git-scm.com/docs>
- git-flight-rules:<https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md>

## Command Line

### 配置

- basics

```bash
git config --global user.name "Preisthe"
git config --global user.email name@qq.com
git config --global init.default branch main
```

- help

```bash
git config -h
git help config
```

### 初始化 Initialize Repository

- new

```bash
git init
```

- clone

```bash
git clone url
```

### 暂存 stage

- checkout

```bash
git status
```

- track

```bash
git add filename
git rm --cached filename #撤销
```

```bash
git add --all
-A
.
```

### .gitignore

忽略文件或文件夹  
*注意*：该文件只能作用于Untracked Files，也就是那些从来没有被 GIT 记录过的文件（自添加以后，从未 add 及 commit 过的文件）。

- `*` 通配多个字符，`**` 通配中间目录（有或无）
- ! 取消忽略
- <https://git-scm.com/docs/gitignore>

如果要忽略已经被git管理的文件，需要先用 git 删除，再添加到 .gitignore 中。

```bash
git rm --cached <file> / -r <dir>
```

确认忽略文件:

```bash
git check-ignore -v file
```

- 若被忽略，则显示信息，且正常退出
- -v 是 verbose

### 提交 commit

- check the uncommited changes

```bash
git diff
```

- commit

```bash
git commit -m "commit message"
```

- 取消staging

```bash
git restore --staged filename
```

- 跳过stage

```bash
git commit -a -m "commit message"
```

- 文件操作

```bash
git rm filename
git restore filename #撤销
git mv old-name new-name
```

### 回滚

- check commit history

```bash
git log
git log --oneline
git log -p
```

- 修改上一次提交信息

```bash
git commit -m "" --amend
```

- 重置至上一次提交

```bash
git reset hashtag
```

*NOTE*: reset 的作用是回到某个提交，但默认是保留那个提交下已经做出的修改，也就是更接近下一个提交的状态，因此适合用于修改 reset 到的后一个提交。  
同时，如果当前提交之后还有原先的其他提交，则会丢失，可用 `git reflog` 恢复

reset 的三种模式：

- soft: 更改已 staged
- mixed(default): 更改未 stage
- hard: 清除这次提交上的所有更改，相当于 checkout

- 显示详细提交信息

```bash
git show id
```

- 查看之前版本

```bash
git checkout id
git checkout head^^  #向前2
head~n  #向前n个版本
```

- 修改提交树**\***

```bash
git rebase -i --root
```

### 分支 branch

#### new

```bash
git branch <name>
git branch #checkout
git switch <name>
```

or directly

```bash
git switch -c newbranch
```

- rename the current branch

```bash
git branch -m new-name
```

#### merge

merge specified branch into the current branch

```bash
git merge -m "message" branch-name
```

- merge conflict 编辑文件解决冲突

#### delete

```bash
git branch -d branch-name
```

## GitHub

1. create a new repository
2. push an existing repository

    ```bash
    git remote add origin <url>
    git branch -M main
    git push -u origin main
    ```

    git 提交时不能与远程仓库有冲突，所以如果有，要先 pull 更新本地，再推送
    或者 -f 强制推送

    Note:*will not push branch*

    ```bash
    git push --all
    ```

3. directly add new file
4. submit new issues
5. submit a pull request and close an issue
6. download from remote

    ```bash
    git fetch
    git merge
    ```

    or simply

    ```bash
    git pull REMOTE
    ```

    也就是说，git pull 其实是 fetch 和 merge 的组合，所以有时不能随意使用 pull
