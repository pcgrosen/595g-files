#!/bin/bash

rm /etc/xinetd.d/intro
kill -USR2 $(pgrep xinetd)
