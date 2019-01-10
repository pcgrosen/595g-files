# No-help

"What if you don't have an execute function or a `"/bin/sh"` string?"

This challenge spawns a simple service on port 5007.

You can connect to it with `$ nc 127.0.0.1 5007`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs ./no-help_bin.

That is, `init.sh` and `run.sh` are unimportant.

Attack ./no-help_bin! Its source is located in no-help.c!
