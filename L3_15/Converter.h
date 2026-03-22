#ifndef CONVERTER_H
#define CONVERTER_H
#include "Currency.h"

class Converter {
   public:
    static double convert(double amount, const Currency& from,
                          const Currency& to);
    ;
};

#endif
