#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>

#define ARRAY_SIZE 11

/* Define "string_user" to be the type `int function(long, long)` */
typedef long (string_user)(long, long);

/* Define number holder */
typedef struct _number_t {
  long num;
  char name[8];
} number_t;

typedef struct _state_t {
  /* Define an array of string pointers */
  number_t *number_storage[ARRAY_SIZE];
  /* Keep track of how many operations have been performed. */
  long ops_performed;
  /* Define a pointer to the current function in use */
  string_user *current_op;
} state_t;

state_t state;

/* functions that can take strings */

long add(long op1, long op2) {
  return op1 + op2;
}

long mul(long op1, long op2) {
  return op1 * op2;
}

long divide(long op1, long op2) {
  if (op2 == 0) {
    exit(1);
  }
  return op1 / op2;
}

/* User interaction functions */

void prompt() {
  printf("> ");
}

long get_num() {
  char buf[32];
  prompt();
  fgets(buf, 32, stdin);
  return strtol(buf, NULL, 10);
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

void make_number() {
  int index = get_index();

  if (state.number_storage[index] != NULL) {
    puts("That index is already taken!");
    exit(1);
  }

  state.number_storage[index] = malloc(sizeof(number_t));

  puts("OK, send a number.");
  prompt();
  state.number_storage[index]->num = get_num();

  puts("OK, send a name.");
  prompt();
  fgets(state.number_storage[index]->name, 8, stdin);
}

void change_number() {
  int index = get_index();

  if (state.number_storage[index] == NULL) {
    puts("That index hasn't been filled!");
    exit(1);
  }

  printf("OK, send a number to fill '%s'.\n", state.number_storage[index]->name);
  prompt();
  state.number_storage[index]->num = get_num();
}

void switch_function() {
  puts("Please select:");
  puts(" 1. add");
  puts(" 2. mul");
  puts(" 3. div");
  puts(" 4. abs");

  switch (get_num()) {
    case 1:
      state.current_op = add;
      break;
    case 2:
      state.current_op = mul;
      break;
    case 3:
      state.current_op = divide;
      break;
    case 4:
      state.current_op = labs;
      break;
    default:
      puts("That's not a valid function!");
      exit(1);
  }
}

void call_function() {
  int op1_index;
  int op2_index;
  long res;

  puts("Which operands would you like to use?");
  op1_index = get_index();

  if (state.number_storage[op1_index] == NULL) {
    puts("That index hasn't been filled!");
    exit(1);
  }

  op2_index = get_index();

  if (state.number_storage[op2_index] == NULL) {
    puts("That index hasn't been filled!");
    exit(1);
  }

  puts("OK, calling . . .");
  res = state.current_op(state.number_storage[op1_index]->num, state.number_storage[op2_index]->num);
  printf("The result was '%ld'.\n", res);

  state.ops_performed++;
  printf("You have now performed '%ld' operations.\n", state.ops_performed);
}

void delete_number() {
  int index = get_index();

  if (state.number_storage[index] == NULL) {
    puts("That index hasn't been filled!");
    exit(1);
  }

  free(state.number_storage[index]);

  /* TODO: NULL out this entry in the array. */
}

int main() {
  int option;

  memset(state.number_storage, 0, sizeof(state.number_storage));

  puts("Welcome!");

  state.ops_performed = 0;
  state.current_op = add;

  while (1) {
    puts("Please select:");
    puts(" 1. Create a new number.");
    puts(" 2. Change a number.");
    puts(" 3. Switch function.");
    puts(" 4. Call function.");
    puts(" 5. Delete a number.");
    puts(" 6. Exit.");

    option = get_num();

    switch (option) {
      case 1:
        make_number();
        break;
      case 2:
        change_number();
        break;
      case 3:
        switch_function();
        break;
      case 4:
        call_function();
        break;
      case 5:
        delete_number();
        break;
      default:
        exit(0);
    }
  }

  return 0;
}
