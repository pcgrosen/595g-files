# Simple Xor

`simple_xor` is an introductory challenge regarding xor encoding.

This challenge spawns a simple service on port 5002.

You can connect to it with `$ nc 127.0.0.1 5002`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs prog.py (in unbuffered mode).

That is, `init.sh` and `run.sh` are unimportant.

Attack prog.py!
