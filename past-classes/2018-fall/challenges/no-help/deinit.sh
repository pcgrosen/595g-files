#!/bin/bash

rm /etc/xinetd.d/no-help
kill -USR2 $(pgrep xinetd)
