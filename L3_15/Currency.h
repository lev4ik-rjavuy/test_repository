#ifndef CURRENCY_H
#define CURRENCY_H
#include <string>

class Currency {
   private:
    double value;
    std::string name;

   public:
    Currency(double value, std::string name);
    double getValue() const;
    std::string getName() const;
};

#endif