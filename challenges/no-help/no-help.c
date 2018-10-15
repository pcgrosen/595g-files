#include <stdio.h>

void print(char *data, int len) {
  fwrite(data, 1, len, stdout);
}

void get(char *out, int len) {
  fgets(out, len, stdin);
}

int main() {
  char buf[8];

  print("Welcome\n", 8);

  get(buf, 0x80);

  return 0;
}
