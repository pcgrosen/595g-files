#include <stdio.h>

int main() {
  char buf[1024];

  fgets(buf, 1024, stdin);

  printf(buf);

  puts("Job's done.");

  return 0;
}
