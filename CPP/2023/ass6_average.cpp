#include <iostream>
#include <vector>
using namespace std;
//I LOVE YOU JARED
int main() {
    //taking input and defining static values
    int length;
    vector<double> numbers; 
    cout << "how many numbers being averaged?"; cin >> length; 
    double total,average;
    //taking input for all elements
    for (int x=0;x<length;x++) {
        double val;
        cout << "enter number " << x + 1 << ": "; 
        cin >> val;  
        numbers.push_back(val);
    };
    //calculating total
    for (int x=0; x<length; x++) {
        total += numbers[x];
    };
    // average
    average = total / length;
    cout << "Your average among " << length << " values with a total of " << total << " is " << average;

    return 0;
};