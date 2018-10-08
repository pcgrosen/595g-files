#!/bin/bash

rm /etc/xinetd.d/read-rop
kill -USR2 $(pgrep xinetd)
