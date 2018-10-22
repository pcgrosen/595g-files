#!/bin/bash

rm /etc/xinetd.d/doubly-inexpensive-hard
kill -USR2 $(pgrep xinetd)
