// ANDREW CHURCH - ALLEN KRUEGER - CIS AM - 12/04/2023
#include <iostream>
using namespace std;

int main(){
    cout << "This is wildly inefficient. I made it divide without division because it would be funny." << endl;
    //taking in input
    int dividend,divisor,quotient,remainder;
    cout << "Dividend:"; cin >> dividend;
    cout << "Divisor:"; cin >> divisor;
    //dividing
    while (dividend/divisor > 0) {
        dividend -= divisor;
        quotient += 1;
    };
    //remainder
    remainder = dividend;
    //output
    cout << "Your quotient is " << quotient << " R" << remainder;
    //the end  
    return quotient; 

};