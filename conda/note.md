# conda 备忘

参考：[官方文档](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)

*2024-3-23*

## 创建虚拟环境

```zsh
conda crate -n <env-name> python=3.9
```

添加包

```zsh
conda create -n myenv numpy pandas
```

## 查看虚拟环境列表

```zsh
conda env list
conda info -e
conda info --env
```

## 确认当前环境

- 命令提示符 如`(base)`
- 虚拟环境列表中带`*`号
- 查看配置信息`conda info`

## 激活/切换虚拟环境

```zsh
conda activate <env-name>
```

回到默认的`base`环境

```zsh
conda activate
```

## 退出虚拟环境

```zsh
conda deactivate
```

*退回至上一次激活的环境*

## 指定环境安装新包

```zsh
conda install -n myenv numpy
```

## 更新

```zsh
conda --version
conda update conda
```

## 复制虚拟环境

```zsh
conda create -n <new> --clone <old>
```

*重命名通过clone+remove实现*

## 删除虚拟环境

```zsh
conda remove -n <env-name> --all
```

*当前虚拟环境不能删除，必须退出之后删除*

## 导出环境

```zsh
conda env export --file name.yaml
```

*注意：文件名与环境名无关*

## 还原导出的环境

```zsh
conda env create -f name.yaml
```

`yml`文件的第一行设置了环境名称
