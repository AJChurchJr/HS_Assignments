#include <iostream>
#include <cmath>


//This program is rather simple.
//It takes four arguments: amount, interest percent, interest rate, and time.
//It then plugs all of those numbers into an equation and displays them, followed by a stupid joke.
//It is just input and output and not much else. 

using namespace std; 
int main()
{
	double moneyAmount, ratePerYear, interestPercent, time;
	cout << "COMPOUNT INTEREST GENERATOR" << endl << "____________________" << endl;
	cout << "How much money do you owe? "; cin >> moneyAmount;
	cout << "How often does interest get applied? "; cin >> ratePerYear;
	cout << "What is the interest percent? "; cin >> interestPercent; interestPercent /= 100;
	cout << "How long are you going to go without paying? "; cin >> time;
	double CI = moneyAmount * (pow((1 + (interestPercent / ratePerYear)), (ratePerYear * time)));
	cout << "You owe $" << CI << endl;
	cout << "The Rothschilds are coming." << endl; (interestPercent / ratePerYear);
	return 0;
}
