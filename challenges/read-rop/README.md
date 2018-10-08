# Read-rop

"What if you don't have an `execve("/bin/sh")` gadget or a `"/bin/sh"` string?"

This challenge spawns a simple service on port 5006.

You can connect to it with `$ nc 127.0.0.1 5006`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs ./read-rop_bin.

That is, `init.sh` and `run.sh` are unimportant.

Attack ./read-rop_bin! Its source is located in read-rop.c!
