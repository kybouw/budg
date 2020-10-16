/* plan.hpp */

#ifndef PLAN_HPP
#define PLAN_HPP

class Plan {
    private:
        //stuff
        std::string name;
        std::vector<LineItem>* line_items;
    public:
        //more stuff
        Plan();
        ~Plan();
        std::string get_name();


};

#endif
