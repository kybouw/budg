#ifndef LINEITEM_HPP
#define LINEITEM_HPP

class LineItem {
    private:
        //stuff
        int budget_value;
        std::string name;
    public:
        //more stuff
        LineItem(int budget_value, std::string name);
        ~LineItem();
};

#endif
