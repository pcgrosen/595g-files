#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


void give_shell() {
  char *argv[2] = {"/bin/sh", NULL};
  execve("/bin/sh", argv, NULL);
}

int main() {
  char buf[16];

  fgets(buf, 0x20, stdin);

  return 0;
}
