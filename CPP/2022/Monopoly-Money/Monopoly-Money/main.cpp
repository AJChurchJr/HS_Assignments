//I will attempt to program this as simply as possible:

/*
 1. Create an array that contains the values for how many of each bill is counted.
    Create an array of the same size that contains the acatual size of each bill.
 example:
    [0,0,0,0,0,0,0]
    [1,5,10,20,50,100,500]
 why:
    This may seem pointless at first but this is because I am going to execute the code in a for-loop.
    Since it will be accessing the bills using a value of i, it should be able to access which bill it is raising the counter to, and the value of the bill.
    This is to prevent hard-coding.
2.
    As said in the "why" part of step 1, use a for-loop to subtract a set amount of the billValue array with the index of i from a dummy of the value.
 After this, print the values using another for-loop.
 
*/

#include <iostream>
using namespace std;
int main() {
    //Variable defining
    int numInput,dummyNum;
    int billCount[7] = {0,0,0,0,0,0,0};
    int billValue[7] = {500,100,50,20,10,5,1};
    //Taking input
    cout << "Please input a number to split: "; cin >> numInput;dummyNum = numInput;
    //Counter
    for (int i=0 ; i<7 ; i++)
    {
        while (1==1)
        {
            if (dummyNum - billValue[i] >= 0) {dummyNum -= billValue[i];billCount[i] += 1;continue;}
            else{break;}
        }
    }
    //Displaying counters
    for (int i=0 ; i<7 ; i++) {cout << "Number of $" << billValue[i] << " bills: " << billCount[i] << endl;}
    return 0;
}
