#include <inttypes.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#ifdef __GLIBC__
# include <malloc.h>
# include <mcheck.h>
#endif

int main(int argc, char ** argv) {

	fprintf(stderr, "pid: %d\n", getpid());

	char buffer[1000];
	while (1) {
		fprintf(stderr, "> ");
		fgets(buffer, sizeof(buffer), stdin);
		char cmd[1000];
		intptr_t arg1, arg2;
		int num = sscanf(buffer, "%s %"SCNiPTR" %"SCNiPTR, cmd, &arg1, &arg2);
		if (strcmp(cmd, "malloc") == 0) {
			void* result = malloc(arg1);
			fprintf(stderr, "==> %p\n", result);
		} else if (strcmp(cmd, "free") == 0) {
			free((void*) arg1);
			fprintf(stderr, "==> ok\n");
		} else if (strcmp(cmd, "show") == 0) {
			if (num == 2) {
				arg2 = 1;
			}
			long * src = (long*) arg1;
			for (int i = 0; i < arg2; i++) {
				fprintf(stderr, "%p: %#16.0lx\n", &src[i], src[i]);
			}
#ifdef __GLIBC__
		} else if (strcmp(cmd, "usable") == 0) {
			fprintf(stderr, "usable size: %zu\n", malloc_usable_size((void*) arg1));
		} else if (strcmp(cmd, "stats") == 0) {
			malloc_stats();
		} else if (strcmp(cmd, "info") == 0) {
			malloc_info(0, stdout);
#endif
		} else {
			puts("Commands: malloc n, free p, show p [n], usable p, stats, info, mprobe [p], mcheck, mcheck_pedantic");
		}
	}
}
