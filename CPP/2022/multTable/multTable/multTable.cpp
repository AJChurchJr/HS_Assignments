#include <iostream>
using namespace std;
int main()
{
	//defining values
	int num, limit;
	//taking input
	cout << "Please enter a number: ";cin >> num;
	cout << "Please enter a Multiplication Table limit: ";cin >> limit;
	//displaying multiplication
	for (int i = 0 ; i <= limit ; ++i){cout << num << " x " << i << " = " << (num * i) << endl;}
}

