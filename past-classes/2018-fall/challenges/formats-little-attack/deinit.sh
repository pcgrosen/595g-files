#!/bin/bash

rm /etc/xinetd.d/formats-little-attack
kill -USR2 $(pgrep xinetd)
