/*
 * budg - my app for budgeting my paychecks
 *
 * Copyright (C) 2020 Kyle Bouwman
 *
 * This file is part of budg.
 *
 * budg is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * budg is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with budg.  If not, see <https://www.gnu.org/licenses/gpl.html>.
 */

#include <cstdio>
#include <string>
#include "budg.hpp"


int main(int argc, char** argv) {

    if(argc == 1) {
        printf("Hello, world!\n");
        return 0;
    }

    int vals = argc - 1;
    uint pennies = 0;
    for(int i = 0; i < vals; i++) {
        pennies += verify_amount(argv[i + 1]);
    }

    printf("Amount entered: %s\n", toDollars(pennies).c_str());

    return 0;
}

uint verify_amount(char* s) {
    return (uint)(std::stod(s) * 100);
}

string toDollars(const uint & pennies) {

    uint dollars = pennies / 100;
    uint cents = pennies % 100;

    string cents_str;
    if(cents < 10) {
        cents_str = "0" + std::to_string(cents);
    }
    else {
        cents_str = std::to_string(cents);
    }

    string s = "$" + std::to_string(dollars) + "." + cents_str;
    return s;
}
