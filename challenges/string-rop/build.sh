#!/bin/sh
gcc string-rop.c -fno-stack-protector -no-pie -o string-rop_bin
