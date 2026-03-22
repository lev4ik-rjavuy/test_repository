#include <iostream>
#include <string>

#include "Converter.h"
#include "Currency.h"

using namespace std;

int main() {
    Currency USD(43.73, "USD");
    Currency EUR(50.69, "EUR");
    Currency UAH(1.0, "UAH");

    cout << "Поточні курси:" << endl;
    cout << "USD: " << USD.getValue() << " " << USD.getName() << endl;
    cout << "EUR: " << EUR.getValue() << " " << EUR.getName() << endl;
    cout << "UAH: " << UAH.getValue() << " " << UAH.getName() << "\n\n";

    double amountToConvert = 100.0;

    cout << "Конвертація " << amountToConvert << " одиниць:" << endl;

    cout << "USD в UAH: " << Converter::convert(amountToConvert, USD, UAH)
         << " UAH" << endl;
    cout << "EUR в UAH: " << Converter::convert(amountToConvert, EUR, UAH)
         << " UAH" << endl;
    cout << "UAH в USD: " << Converter::convert(amountToConvert, UAH, USD)
         << " USD" << endl;
    cout << "UAH в EUR: " << Converter::convert(amountToConvert, UAH, EUR)
         << " EUR" << endl;

    return 0;
}