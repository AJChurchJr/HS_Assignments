// areaCalc.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cmath>
/*
create variables
take input asking for what shape you want the area of (as a number, to prevent misspellings)
depending on the shape, var1, var2, or both, will be used, with it asking for different values depending on the shape
perform different calculations with existing variables based off of the shape selection
*/
int main()
{
	bool run = true;
	while (run == true)
	{ 
		int selection;
		double var1,var2,result;

		std::cout << "(1) rectangle || (2) square || (3) circle || (4) triangle" << "\n" << "Make your selection now:";
		std::cin >> selection;
	
		if (selection == 1){
			std::cout << "input length: "; std::cin >> var1;
			std::cout << "input width: "; std::cin >> var2;
			result = var1 * var2;
			std::cout << "The area of your rectangle is: " << result << std::endl;
		}
		else if (selection == 2) {
			std::cout << "input side length: "; std::cin >> var1;
			result = pow(var1, 2);
			std::cout << "The area of your square is: " << result << std::endl;
		}
		else if (selection == 3) {
			std::cout << "input radius: "; std::cin >> var1;
			result = 3.14 * pow(var1,2);
			std::cout << "The area of your circle is: " << result << std::endl;
		}
		else if (selection == 4) {
			std::cout << "input base length: "; std::cin >> var1;
			std::cout << "input height: "; std::cin >> var2; std::cout;
			result = 0.5 * var1 * var2;
			std::cout << "The area of your triangle is: " << result << std::endl;
		}

		else(run = false);
		std::cout << std::endl;
	}

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
