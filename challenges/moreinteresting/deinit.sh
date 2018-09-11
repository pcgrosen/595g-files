#!/bin/bash

rm /etc/xinetd.d/moreinteresting
kill -USR2 $(pgrep xinetd)
