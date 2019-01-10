#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


void give_shell() {
  char *argv[2] = {"/bin/sh", NULL};
  execve("/bin/sh", argv, NULL);
}

int main() {
  char buf[8];

  puts("Hello! I'm learning C! What's your name?");
  fgets(buf, 0x40, stdin);

  printf("Hi %s!\n", buf);

  return 0;
}
