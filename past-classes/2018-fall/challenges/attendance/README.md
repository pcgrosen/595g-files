# Attendance

I will be using this challenge to determine whether or not you are participating, so be sure to do it!

This challenge spawns a simple service on port 5001.

You can connect to it with `$ nc 127.0.0.1 5001`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs prog.py (in unbuffered mode).

That is, `init.sh` and `run.sh` are unimportant.

Attack prog.py!
