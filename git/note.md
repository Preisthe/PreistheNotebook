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

创建.gitignore文件
忽略文件或文件夹  

- `*` 通配多个字符，`**` 通配中间目录（有或无）
- ! 取消忽略
- <https://git-scm.com/docs/gitignore>

```bash
git check-ignore -v file
```

### 提交 commit

- check the unstaged changes

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

- 显示详细提交信息

```bash
git show id
```

- 查看之前版本

```bash
git checkout id
git checkout head^^  #向前2
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
