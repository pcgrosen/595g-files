#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char binsh[] = "/bin/sh";

void give_shell(char *command) {
  char *argv[2] = {command, NULL};
  execve(command, argv, NULL);
}

asm("helper:     \n"
      "pop %rsi  \n"
      "pop %rdi  \n"
      "ret");

int main() {
  char buf[8];

  puts("You know the drill . . . ");
  fgets(buf, 0x40, stdin);

  return 0;
}
