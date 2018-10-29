#!/bin/bash

rm /etc/xinetd.d/calculator-for-sale
kill -USR2 $(pgrep xinetd)
