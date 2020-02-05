/**
 * budg
 * budg.c
 * by Kyle Bouwman
 * subject to MIT License (see LICENSE)
 * 
 * a script for budgeting my paychecks
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* Usage string */
const char* USAGE = "Usage: budg <amount>\n e.g. >$ budg 123.45\n";
/* Name of the config file */
const char* CFGFILE = "/.config/budg.ini";

/* main function */
int main(int argc, char ** argv) {

    /* verify args */
    if(argc != 2) {
        printf("ERROR: Invalid Argument(s)\n");
        printf("%s", USAGE);
        exit(1);
    }

    /* parse arg */
    double amount = atof(argv[1]);

    /* DEBUG print amount passed in */
    printf("amount: %.2f\n", amount);

    /* get the path to the config file */
    // get path to HOME
    char* HOME = getenv("HOME");
    // allocate memory for file path
    char* file = malloc(strlen(HOME) + strlen(CFGFILE) + 1);
    // concat home with filename inside file
    strcpy(file, HOME);
    strcat(file, CFGFILE);

    /* DEBUG print the file path */
    printf("config path: %s\n", file);

    free(file);
    return 0;

}