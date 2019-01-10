#!/bin/bash

rm /etc/xinetd.d/simple_xor
kill -USR2 $(pgrep xinetd)
