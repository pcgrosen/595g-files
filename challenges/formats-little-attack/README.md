# Formats-little-attack

"Format strings: they're safe, right?"

This challenge spawns a simple service on port 5011.

You can connect to it with `$ nc 127.0.0.1 5011`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs ./formats-little-attack_bin.

That is, `init.sh` and `run.sh` are unimportant.

Attack ./formats-little-attack_bin! Its source is located in formats-little-attack.c!
