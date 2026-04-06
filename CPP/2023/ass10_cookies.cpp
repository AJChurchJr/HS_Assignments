// Andrew Chruch - Allen Krueger - CIS AM 

#include <iostream>
using namespace std;

int main(){
    //creating values and defining them
    int length,total=0;
    double price,avg,totalprice;
    cout << "How many students are selling cookies? "; cin >> length;
    cout << "How much money does each box of cookies sell for? "; cin >> price;
    //creating lists
    string *names = new string[length];
    int *amounts = new int[length];
    //Iterating through lists and adding amounts
    for (int i = 0; i < length ; i++) {
        cout << "--New Student--" << endl;
        cout << "Name?"; cin >> names[i];
        cout << "Amount sold?"; cin >> amounts[i];
    };
    //Final values
    for (int i=0; i<length;i++){total += amounts[i];};
    avg = total/length;
    totalprice = total * price;
    cout << "You sold a total of " << total << " cookies." << endl << "You made a total of $" << totalprice << endl << "Each student sold an average of " << avg << " cookies." << endl; 
    //preventing memory leak
    delete names;
    delete amounts;
}