# Doubly-inexpensive-hard

"I don't need to clean up my malloc'ed pointers, do I?"

This challenge spawns a simple service on port 5009.

You can connect to it with `$ nc 127.0.0.1 5009`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs ./doubly-inexpensive-hard_bin.

That is, `init.sh` and `run.sh` are unimportant.

Attack ./doubly-inexpensive-hard_bin! Its source is located in doubly-inexpensive-hard.c!
