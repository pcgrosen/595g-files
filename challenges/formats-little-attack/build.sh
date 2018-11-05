#!/bin/sh
gcc formats-little-attack.c -Wno-format-security -fno-stack-protector -no-pie -o formats-little-attack_bin
