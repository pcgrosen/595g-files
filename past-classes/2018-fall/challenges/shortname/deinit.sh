#!/bin/bash

rm /etc/xinetd.d/shortname
kill -USR2 $(pgrep xinetd)
