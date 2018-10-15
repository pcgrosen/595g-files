#!/bin/sh
gcc read-rop.c -fno-stack-protector -no-pie -o read-rop_bin
