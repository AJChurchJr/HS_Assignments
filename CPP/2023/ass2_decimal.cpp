#include <iostream>
#include <iomanip> // formatting floting-point numbers with 1 decimal place
using namespace std;

int main() {
    // defining values
    auto m1 = 5, m2 = 7;
    auto d1  = 3.7, d2=8.0;
    cout << "\n\n Display arithmetic operations with mixed data type :\n";

    // setprecision is a part of iomanip in c++, which sets the OUTPUT'S precision
    // usually it is put at the end of cout, however here it is put next to the name 'fixed'
    // this means, likely, that it is applied to every cout statement
    cout << fixed << setprecision(1);

    // output
    cout << " " << m1 << " + " << m1 << " = " << m1+m1 << endl;
    cout << " " << m1 << " + " << m2 << " = " << m1+m2 << endl;
    cout << " " << m1 << " + " << d1 << " = " << m1+d1 << endl;
    cout << " " << m1 << " + " << d2 << " = " << m1+d2 << endl;
    cout << " " << m2 << " + " << m1 << " = " << m2+m1 << endl;
    cout << " " << m2 << " + " << m2 << " = " << m2+m2 << endl;
    cout << " " << m2 << " + " << d1 << " = " << m2+d1 << endl;
    cout << " " << m2 << " + " << d2 << " = " << m2+d2 << endl;
    cout << " " << d1 << " + " << m1 << " = " << d1+m1 << endl;
    cout << " " << d1 << " + " << m2 << " = " << d1+m2 << endl;
    cout << " " << d1 << " + " << d1 << " = " << d1+d1 << endl;
    cout << " " << d1 << " + " << d2 << " = " << d1+d2 << endl;
    cout << " " << d2 << " + " << m1 << " = " << d2+m1 << endl;
    cout << " " << d2 << " + " << m2 << " = " << d2+m2 << endl;
    cout << " " << d2 << " + " << d1 << " = " << d2+d1 << endl;
    cout << " " << d2 << " + " << d2 << " = " << d2+d2 << endl;


    //main loop -- playground
    cout << "WHILE LOOP EXAMPLE -- PRESS CTRL+C TO EXIT" << endl;
    while (true) {
        //input
        cout << "Enter an integer: "; cin >> m1;
        cout << "Enter another integer: "; cin >> m2;
        //output
        cout << " " << m1 << " + " << m2 << " = " << m1+m2 << endl;
        cout << " " << d1 << " + " << d2 << " = " << d1+d2 << endl;
    };
    
    return 0;
}