// ANDREW CHURCH - ALLEN KRUEGER - CIS AM - 12/04/2023
// I AM NOT GETTING THE OUTPUT YOU ARE GETTING. HOWEVER, THE SCALENE TRIANGLE CALCULATOR SAYS I AM CORRECT.
#include <iostream>
#include <cmath>
using namespace std;


long double calc_area(double a,double b,double c){
    double S = (a + b + c) / 2;
    long double A = sqrt(S*(S-a)*(S-b)*(S-c));
    return A;
};



int main(){
    // 
    double a,b,c; 
    cout << "enter side 1:"; cin >> a;
    cout << "enter side 2:"; cin >> b;
    cout << "enter side 3:"; cin >> c;
    long double area = calc_area(a=a,b=b,c=c);
    cout << "Your area is:" << area;
};