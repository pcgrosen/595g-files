# Shortname

Johnny the Programmer says:
    "Welcome to my first C program! I can assume your name is short, right?"

This challenge spawns a simple service on port 5003.

You can connect to it with `$ nc 127.0.0.1 5003`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs ./cookiemonster_bin.

That is, `init.sh` and `run.sh` are unimportant.

Attack ./cookiemonster_bin! Its source is located in cookiemonster.c!
