/* budg.hpp */

#ifndef BUDG_HPP
#define BUDG_HPP

class Budg {
    private:
        Config* cfg;
        Plan* plan;

        /** in pennies */
        int total_income;

    public:
        Budg();
        ~Budg();
        void pass_args(int argc, char** argv);
        void add_income(int income);
        int get_total_income();
        std::string get_total();
        Plan* get_plan();

};

std::string to_dollars(int pennies);

#endif
