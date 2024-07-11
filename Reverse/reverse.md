# Reverse

## 常用命令

### 编译指令

gcc -> as ->
clang -> llvm-mc
clang -save-temps
hello.bc # llvm IR 二进制表达

### 查看文件信息

file a.elf
objdump -d a.elf # 反汇编
readelf -a a.elf # 查看文件信息
ldd a.elf # 查看依赖库（链接的库）

### 进程

ps / ps -a
pidof a.out # 查看进程号
cd proc/pid # 进入进程目录
cat maps # 查看进程内存映射

## 调试

### 静态调试

strace a.out # 查看系统调用
*可以通过 man \<function\> 查看系统调用手册*
ltrace # 查看库函数调用
*ltrace 只对动态链接的程序有效*

### 动态调试

#### gdb

run # 启动调试
start # 一样，但会停在 main 开头
info # 查看各种信息
info registers # 查看寄存器
info proc maps # 查看进程内存映射
dissass main
b *0x804849b # 在地址处下断点
stepi # 单步执行

## 常用思路

对于符号恢复的静态 or 动态链接目标

- 关注特定常量和字符串
- 关注输入和输出函数
- 关注分支、比较指令
- 关注可能涉及加密解密的特殊运算（位运算、异或、取余）

f5 反编译
