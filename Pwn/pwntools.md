# Pwn

context.log_level = 'debug'
context.arch = 'amd64'

p = process("./login_me")
print(p.recv())

username = b"user"
p.send(username)

## gdb 调试

gdb -p pid

## shellcode

shellcrafts

## 连接

p = remote("IP", PORT)

from wstube import websocket
p = websocket("wss://...")

## 专题

gdb 插件 gef
