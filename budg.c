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

    /* print amount passed in */
    printf("%.2f\n", amount);
}