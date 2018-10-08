#!/bin/bash

rm /etc/xinetd.d/string-rop
kill -USR2 $(pgrep xinetd)
