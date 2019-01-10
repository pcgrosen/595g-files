#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


void give_shell(int are_you_leet) {
  char *argv[2] = {"/bin/sh", NULL};
  if (are_you_leet == 0x31337) {
    execve("/bin/sh", argv, NULL);
  }
}

asm("helper:     \n"
      "pop %rsi  \n"
      "pop %rdi  \n"
      "ret");

int main() {
  char buf[16];

  fgets(buf, 0x40, stdin);

  return 0;
}
