// PostageCalc.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

int main()
{
	double postageWeight, postageCost = 0, tempPostWeight;
	char deliveryType;

	while (1==1)
	{
		postageCost = 0;
		cout << "Please enter the weight, in grams, of your postage item: "; cin >> postageWeight; cout << endl;
		cout << "Please enter your delivery type (N) Next-Day (S) Speed Post 2-Day (R) Regular 3-5-Day: "; cin >> deliveryType; cout << endl;

		if (postageWeight <= 50) { postageCost += 100; }
		else if (postageWeight <= 100) { postageCost += 180; }
		else if (postageWeight <= 250) { postageCost += 250; }
		else if (postageWeight <= 500)
		{
			tempPostWeight = postageWeight - 250; //TempPostCost 
			postageCost += 250;
			while (tempPostWeight > 0)
			{
				postageCost += 50;
				tempPostWeight -= 50;
			}
		}
		else if (postageWeight <= 1000) //does the same as 500 but only adds 25 to the cost
		{
			tempPostWeight = postageWeight - 500; //TempPostCost 
			postageCost += 500;
			while (tempPostWeight > 0)
			{
				postageCost += 25;
				tempPostWeight -= 50;
			}
		} 

		if (deliveryType == 'N' || deliveryType == 'n') { postageCost += 550; }
		else if (deliveryType == 'S' || deliveryType == 's') { postageCost += 325; }
		else if (deliveryType == 'R' || deliveryType == 'r') { postageCost += 50; }
		else { postageCost += 50; } //defaults to regular delivery

		cout << "Your total comes to about " << postageCost << " cents." << endl;

	}
	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
