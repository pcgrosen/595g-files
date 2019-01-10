#!/bin/bash

rm /etc/xinetd.d/doubly-inexpensive
kill -USR2 $(pgrep xinetd)
