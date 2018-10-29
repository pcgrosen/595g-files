# Calculator-for-sale

"This calculator is pretty simple, and, even if there is a double free, it's useless!"

This challenge spawns a simple service on port 5010.

You can connect to it with `$ nc 127.0.0.1 5010`.

`init.sh` sets up the xinetd service to run `run.sh` on connection.

`run.sh` runs ./calculator-for-sale_bin.

That is, `init.sh` and `run.sh` are unimportant.

Attack ./calculator-for-sale_bin! Its source is located in calculator-for-sale.c!
