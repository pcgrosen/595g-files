#!/bin/bash

rm /etc/xinetd.d/attendance
kill -USR2 $(pgrep xinetd)
