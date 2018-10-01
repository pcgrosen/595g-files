# pwntools

pwntools is a python package for performing ctf-related tasks.

You can import all of its functionality into the global namespace with:

``` python
from pwn import *
```

## Interfacing with a processes and remotes

One of its most useful features is its suite for interacting with programs both local and remote. pwntools exposes the same API for both cases, so you can quickly switch from one to the other just by swapping out your opening line.

### Opening processes and connections

``` python
# Spawn a local process
r = process("./shortname")

# Connect to a remote socket
r = remote("10.0.10.10", 5003)
```

### Talking to programs

pwntools has several helper funtions for talking to processes and remotes.

``` python
# Receive up to 5 bytes
content = r.recv(5)

# Receive exactly 5 bytes
content = r.recvn(5)

# Receive up to and including a newline ("\n")
content = r.recvline()

# Buffer incoming data until it matches a regex
content = r.recvregex(some_regex)


# Send data
r.send(data)

# Send data + "\n"
r.sendline(data)


# Provide a netcat-esque user-interface to the connection (use this when you think you have a shell!)
r.interactive()
```

### Debugging a connection

pwntools will log all transmitted/received data on a connection if you increase its verbosity. To do so, use:

``` python
# (context is a global variable that is imported with the pwntools import statement)
context.log_level = "DEBUG"
```

### Attaching GDB (local processes only)

You can easily attach gdb to a local process with:

``` python
attach(r)
```

## Tips and tricks

### Simple switching from local to remote functionality

It's oftentimes useful to wrap local/remote specific operations in an if statement so that a single variable can allow you to switch from local to remote mode (useful for debugging locally and then switching to the remote):

``` python
LOCAL = True

if LOCAL:
    r = process("./shortname")
else:
    r = remote("10.0.10.10", 5003)

# ...

if LOCAL:
    attach(r)
else:
    # pass is a statement that does nothing
    pass
```

### Remember to send newlines

Many C functions such as `fgets` expect newlines at the end of input. Therefore, be sure to use `sendline`:

``` python
# Will hang if the program is using fgets
r.send(my_payload)
r.recvuntil("Enter more data: ")

# Instead, be sure to send a newline to cause fgets to return
r.sendline(my_payload)
r.recvuntil("Enter more data: ")
```

### Should something else be here?

Let me know and I'll add it!
