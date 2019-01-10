# angrop

angrop is a tool to assist with finding ROP gadgets and building ROP chains.

## Initialization

To begin, you must import angr and angrop and tell angrop to analyze the binary.

``` python
# Import packages
import angr
import angrop

# Create angr project
p = angr.Project("./my_binary")

# Initialize angrop on the project
rop = p.analyses.ROP()

# Tell angrop to find gadgets within the binary
rop.find_gadgets()
```

## Building chains

Chains are python objects that represent ROP operations. They can be added together to form longer chains.

Most of the time, you'll only use `func_call`.

```python
# Call a function by symbol
chain  = rop.func_call("func1", [arg1, arg2])

# Call a function by address
address = 0x400500
chain += rop.func_call(address, [arg10, arg20])

# Set particular registers (typically only used when func_call isn't enough)
chain += rop.set_regs(rdi=5)


# These gadgets are rarely present -- if they are, good for you!
#    But if not, you'll need to use function calls to emulate them (e.g. via fgets or read)

# Write a string to an address in memory
chain += rop.write_to_mem(0x61b100, b"/bin/sh\0")

# Add a value to an address in memory
chain += rop.add_to_mem(0x61b100, 0x12345678)
```

## Creating a payload

angrop can't determine how much padding is needed at the start of a chain, so you will need to write that portion yourself; it simply assumes that the first eight bytes of the chain will overlap with the original return address.

``` python
padding = ("a" * 16)
payload = padding + chain.payload_str()

r.sendline(payload)
```
