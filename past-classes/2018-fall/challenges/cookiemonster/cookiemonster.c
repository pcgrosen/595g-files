#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void give_shell() {
  char *argv[2] = {"/bin/sh", NULL};
  execve("/bin/sh", argv, NULL);
}

int main() {
  size_t values[8] = {0x59, 0x147, 0x964, 0x82,
                      0x58, 0x753, 0x234, 0x21};
  int index;
  char buf[8];

  puts("I am a connoisseur of fine values.");
  puts("I have some values for your inspection . . .");
  puts("(Inspect -1 to exit.)");

  while (1) {
    printf("Which would you like to inspect? > ");
    fgets(buf, 7, stdin);
    index = atoi(buf);
    if (index == -1) {
      break;
    }
    printf("Index %d contains 0x%zx.\n", index, values[index]);
  }

  puts("Oh, and just so I know, what's your name?");
  fgets(buf, 0x40, stdin);

  puts("Perfect. See you next time.");

  return 0;
}
