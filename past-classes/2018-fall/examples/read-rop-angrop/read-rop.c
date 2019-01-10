#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char seemingly_useless_buffer[] = {0, 0, 0, 0, 0, 0, 0, 0};

void give_shell(char *command) {
  char *argv[2] = {command, NULL};
  execve(command, argv, NULL);
}

void read_data(char *buf, int len) {
  fgets(buf, len, stdin);
}

asm("helper:     \n"
      "pop %rsi  \n"
      "pop %rdi  \n"
      "ret");

int main() {
  char buf[8];

  puts("Hahaha, there's no \"/bin/sh\" to save you now!");

  read_data(buf, 0x80);

  return 0;
}
