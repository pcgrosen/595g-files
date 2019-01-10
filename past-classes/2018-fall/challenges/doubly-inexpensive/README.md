# Doubly-inexpensive

"I don't need to clean up my malloc'ed pointers, do I?"

This challenge spawns a simple service on port 5008.

You can connect to it with `$ nc 127.0.0.1 5008`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs ./doubly-inexpensive_bin.

That is, `init.sh` and `run.sh` are unimportant.

Attack ./doubly-inexpensive_bin! Its source is located in doubly-inexpensive.c!
