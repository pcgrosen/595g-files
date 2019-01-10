#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

#define ARRAY_SIZE 10

/* Define an array of string pointers */
char *string_storage[ARRAY_SIZE];

/* Define "string_user" to be the type `void function(char *)` */
typedef void (string_user)(const char *);

/* Define the struct that will hold our functions */
struct function_holder {
  string_user *func;
  unsigned long func_id;
};

/* Define an array of pointers function_holders */
struct function_holder *func_storage[ARRAY_SIZE];

/* functions that can take strings */

void standard_print(const char *string) {
  printf("The string was: '%s'\n", string);
}

void double_print(const char *string) {
  printf("Here's the string TWICE: '%s', '%s'\n", string, string);
}

/* print n bytes from the string,
   where n is the value of the first byte in the string */
void print_n(const char *string) {
  char num_to_print = string[0];
  const char *rest_of_string = &string[1];
  fwrite(rest_of_string, num_to_print, 1, stdout);
}

/* User interaction functions */

void prompt() {
  printf("> ");
}

int get_num() {
  char buf[32];
  prompt();
  fgets(buf, 32, stdin);
  return atoi(buf);
}

int get_index() {
  int index;

  puts("Please specify an index.");
  index = get_num();

  if (index < 0 || index >= ARRAY_SIZE) {
    puts("That index isn't valid . . .");
    exit(1);
  }

  return index;
}

void make_string() {
  int index = get_index();

  if (string_storage[index] != NULL) {
    puts("That index is already taken!");
    exit(1);
  }

  string_storage[index] = malloc(16);

  puts("OK, send data to put there.");
  prompt();
  fgets(string_storage[index], 16, stdin);
}

void make_function() {
  int index = get_index();
  int num;
  string_user *func;

  if (func_storage[index] != NULL) {
    puts("That index is already taken!");
    exit(1);
  }

  func_storage[index] = malloc(16);

  puts("Please select:");
  puts(" 1. standard_print");
  puts(" 2. double_print");
  puts(" 3. print_n");
  puts(" 4. puts");

  switch (num = get_num()) {
    case 1:
      func = standard_print;
      break;
    case 2:
      func = double_print;
      break;
    case 3:
      func = print_n;
      break;
    case 4:
      func = puts;
      break;
    default:
      puts("That's not a valid function!");
      exit(1);
  }

  func_storage[index]->func = func;
  func_storage[index]->func_id = num;
}

void call_function() {
  int func_index;
  int string_index;

  puts("Which function would you like to call?");
  func_index = get_index();

  if (func_storage[func_index] == NULL) {
    puts("That index hasn't been filled!");
    exit(1);
  }

  printf("OK, calling function %lx.\n", func_storage[func_index]->func_id);
  puts("Which string would you like to pass?");
  string_index = get_index();

  if (string_storage[string_index] == NULL) {
    puts("That index hasn't been filled!");
    exit(1);
  }

  puts("OK, calling . . .");
  func_storage[func_index]->func(string_storage[string_index]);
}

void delete_string() {
  int index = get_index();

  if (string_storage[index] == NULL) {
    puts("That index hasn't been filled!");
    exit(1);
  }

  free(string_storage[index]);

  /* TODO: NULL out this entry in the array. */
}

int main() {
  int option;

  memset(string_storage, 0, sizeof(string_storage));
  memset(func_storage, 0, sizeof(func_storage));

  puts("Welcome!");

  while (1) {
    puts("Please select:");
    puts(" 1. Create a new string.");
    puts(" 2. Create a new function.");
    puts(" 3. Call a function with a string.");
    puts(" 4. Delete a string.");
    puts(" 5. Exit.");

    option = get_num();

    switch (option) {
      case 1:
        make_string();
        break;
      case 2:
        make_function();
        break;
      case 3:
        call_function();
        break;
      case 4:
        delete_string();
        break;
      default:
        exit(0);
    }
  }

  return 0;
}
