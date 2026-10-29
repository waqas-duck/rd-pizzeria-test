#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int load_recipe(const char *path) {
    FILE *fp = fopen(path, "r");
    char line[128];
    if (fp == NULL) {
        return -1;
    }
    while (fgets(line, sizeof line, fp)) {
        puts(line);
    }
    return 0;
}

char *copy_name(const char *name) {
    char *buf;
    buf = malloc(strlen(name) + 1);
    strcpy(buf, name);
    return buf;
}
