# String-rop

"What if you don't have an `execve("/bin/sh")` gadget?"

This challenge spawns a simple service on port 5005.

You can connect to it with `$ nc 127.0.0.1 5005`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs ./string-rop_bin.

That is, `init.sh` and `run.sh` are unimportant.

Attack ./string-rop_bin! Its source is located in string-rop.c!
