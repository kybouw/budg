/* lineitem.cpp */

#include <string>
#include "lineitem.hpp"

LineItem::LineItem(double budget_value, std::string name) {
    this->budget_value = budget_value;
    this->name = name;
}

LineItem::~LineItem() {
}

double LineItem::get_budget_value() {
    return this->budget_value;
}

void LineItem::set_budget_value(double a) {
    this->budget_value = a;
}

std::string LineItem::get_name() {
    return this->name;
}

void LineItem::set_name(std::string n) {
    this->name = n;
}


