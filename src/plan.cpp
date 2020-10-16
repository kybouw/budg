/* plan.cpp */

#include <string>
#include <vector>
#include "lineitem.hpp"
#include "plan.hpp"

Plan::Plan() {
    name = "untitled plan";
    line_items = new std::vector<LineItem>();
}

Plan::~Plan() {
    delete line_items;
}

std::string Plan::get_name() {
    return this->name;
}


