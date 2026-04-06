#include <iostream>
using namespace std;

int main() {
    // ANDREW CHURCH - ALLEN KRUEGER - CIS AM
    double capacity,mpg,cost;
    cout << "How much gas does your car hold? "; cin >> capacity;
    cout << "How many miles per gallon does your car get? "; cin >> mpg;
    cout << "How much does gas cost per gallon? "; cin >> cost;
    cout << "Your car can drive " << capacity * mpg << " miles without refueling." << endl;
    cout << "It costs " << cost * capacity << "$ to refuel your car." << endl;


    return 0;
};

/*
Input: 10,10,4.33
Output: 100, 43.3
*/