#include <iostream>
using namespace std;
int main()
{
    int num, output[2] = {0,0};cout << "Please enter your number: "; cin >> num; //definition, inputs
    while (num!=1&&num!=(-1)) //checking to see if the value is either 1 or -1: negative input validation
    {
        output[0]++; //counter raising
        if (num>output[1]){output[1]=num;} //highest number check
        if (num%2 == 0) {num /= 2;}  //dividing by 2 if even
        else {if(num<0){num*=3;num-=1;} else {num*=3;num+=1;}} //multiplying by 3 and adding/subtracting 1 if odd: negative input validation
        cout << "COUNTER:" << output[0] << "|HIGEST:" << output[1] << "|CURRENT:" << num << endl; //displaying
    }
    cout << "Number was solved in: " << output[0] << " inputs and the highest value reached was " << output[1] << endl;return 0; //output
}
