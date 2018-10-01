#!/bin/bash

rm /etc/xinetd.d/cookiemonster
kill -USR2 $(pgrep xinetd)
