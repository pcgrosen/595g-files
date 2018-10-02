# Cookiemonster

"I hope you like cookies . . . You'll need one for this challenge."

This challenge spawns a simple service on port 5004.

You can connect to it with `$ nc 127.0.0.1 5004`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs ./cookiemonster_bin.

That is, `init.sh` and `run.sh` are unimportant.

Attack ./cookiemonster_bin! Its source is located in cookiemonster.c!
