#include <iostream>
#include <cmath>
using namespace std;
int main() {
    // ANDREW CHURCH - ALLEN KRUEGER - CIS AM
    //taking input and creating values
    int size;
    cout << "How many inputs?"; cin >> size;
    double *list = new double[size];
    double total = 0.0;
    //iterating through with inputs
    for (int i=0;i<size;i++) {
        cout << "Enter a number: "; cin >> list[i];
    };
    //adding all values
    for (int i=0;i<size;i++) {
        total += list[i];
    };
    //rounding total
    cout << "Your rounded total is: " << round(total) ;
    return 0;
}


/*
Input: 5 (amount), 1.22,2.33,4.55,5.66,7.77
Output: Your rounded total is: 22
*/