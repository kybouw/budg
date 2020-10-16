/* lineitem.cpp */

#include <string>
#include "lineitem.hpp"

LineItem::LineItem(int budget_value, std::string name) {
    this->budget_value = budget_value;
    this->name = name;
}

LineItem::~LineItem() {
}
