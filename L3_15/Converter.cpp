#include "Converter.h"

double Converter::convert(double amount, const Currency& from,
                          const Currency& to) {
    return amount * from.getValue() / to.getValue();
}