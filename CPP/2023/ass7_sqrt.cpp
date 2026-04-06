#include <iostream>
#include <cmath>
using namespace std;


int main() {
    //taking input
    int num; cout << "num:"; cin >> num;
    int curPow = 0,curVal=pow(2,curPow);
    //raising two to a power until it is either equal to the number or exceeds it
    while (curVal < num) {
        curPow += 1;
        curVal = pow(2,curPow);
        //output if the power is found
        if (num == curVal) {
            cout << "Your number is two to the power of " << curPow << "!";
            return 0; 
        };
    };
    // if exceeded, returns 0
    cout << "Your number is not a power of two.";
    return 0;
};


/*
Input: 1 -> 2 to the power of 0
Input: 2 -> 2 to the power of 1
Input: 3 -> Not a power of 2
Input: 128 -> 2 to the power of 7
Input: 999 -> Not a power of two
*/