# Pwn

context.log_level = 'debug'
context.arch = 'amd64'

p = process("./login_me")
print(p.recv())

username = b"user"
p.send(username)