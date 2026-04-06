// Program by Andrew Church
// Instructor: Mr. Allen Krueger of Computer Information Science AM
// Created November 21, 2023

#include <iostream>
#include <cmath> // (2) cmath is needed to bring the square root function to availability
#include <iomanip>
using namespace std;

int main() {
    cout << "TRIANGULAR AREA CALCULATORATOR\n";

    //defining values; honestly i really wish they were a list
    double side1,side2,side3;
    //taking input for values
    cout << "Enter side 1:"; cin >> side1;
    cout << "Enter side 2:"; cin >> side2;
    cout << "Enter side 3:"; cin >> side3;
    //figuring out what s is
    double s = (side1+side2+side3)/2;
    //output
    double area = sqrt((s)*(s-side1)*(s-side2)*(s-side3));
    cout << "\nArea is:" << area;
    //this was run, compiled, and bugtested by me so it should work
    return 0;
}
