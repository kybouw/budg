/* lineitem.hpp */

#ifndef LINEITEM_HPP
#define LINEITEM_HPP

class LineItem {
    private:
        //stuff

        /*
         * budget_value is a decimal value representing the percentage
         * of the budget that will be allocated to this LineItem.
         * 0 <= budget_value <= 1
         */
        double budget_value;

        /* if you want to name your plan */
        std::string name;

    public:
        //more stuff
        LineItem(double budget_value, std::string name);
        ~LineItem();
        double get_budget_value();
        void set_budget_value(double a);
        std::string get_name();
        void set_name(std::string n);
};

#endif
