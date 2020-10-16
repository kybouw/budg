/* budg.cpp
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

#include <iostream>
#include <string>
#include <vector>
#include "lineitem.hpp"
#include "plan.hpp"
#include "config.hpp"
#include "budg.hpp"


int main(int argc, char** argv) {

    Budg session = Budg();
    session.pass_args(argc - 1, argv + 1);

    std::cout << "Loading Session..." << std::endl;
    std::cout << "Plan name: " << session.get_plan()->get_name() << std::endl;

    std::cout << "Amount entered: " << session.get_total() << std::endl;

    return 0;
}

Budg::Budg() {
    cfg = new Config();
    plan = new Plan();
    total_income = 0;
}

Budg::~Budg() {
    delete cfg;
    delete plan;
}

void Budg::pass_args(int argc, char** argv) {
    for(int i = 0; i < argc; ++i) {
        total_income += std::stod(argv[i]) * 100;
    }
}

int Budg::get_total_income() {
    return total_income;
}

std::string Budg::get_total() {
    return to_dollars(total_income);
}

std::string to_dollars(int pennies) {

    int dollars = pennies / 100;
    int cents = pennies % 100;

    std::string dollar_str = std::to_string(dollars);
    std::string cents_str = std::to_string(cents);

    // add leading zero to decimal part
    if(cents < 10) cents_str = "0" + cents_str;

    return "$" + dollar_str + "." + cents_str;
}

Plan* Budg::get_plan() {
    return this->plan;
}
