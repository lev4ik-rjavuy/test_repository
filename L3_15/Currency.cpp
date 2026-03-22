#include "Currency.h"

Currency::Currency(double value, std::string name) : value(value), name(name) {}

double Currency::getValue() const { return value; }
std::string Currency::getName() const { return name; }