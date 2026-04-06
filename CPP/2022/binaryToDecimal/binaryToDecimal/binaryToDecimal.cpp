
/*PSEUDOCODE

1. definitions, input
2. while-loop to check and see what the largest digit is
	a. repeatedly multiply a number by 2
	b. if the number ever goes above the input number, stop the loop
	c. take the last number to fit in (i'll call it X) as a reference for which digit to start with, and what number to divide first
3. Convert to get final number
	a. subtract input by X
	b. another loop:
		a. move to previous digit, divide X by 2
		b. stop loop if X goes below 1
		c. if X is 1, and the digit is not 1 (or 0 if you're talking about list index), there has been an error.
4. display final number


*/

#include <iostream>
using namespace std;

string convertDecBin(int input = 0)
{
	//definitions and input
	int solution;

	//creating the highest possible number needed
	//digit starts at 0 because of index stuff, so please note that if things look off
	int digit = 0, subVal = 1;
	while (subVal < input) { subVal *= 2; digit += 1; }

	//creating digit max length for value
	int highestDigit = digit + 1; int* binArr = new int[highestDigit];

	//TEST CODE
	/*cout << "HIGHEST SUBVAL: " << subVal << endl;
	cout << "HIGHEST DIGIT -1: " << digit << endl;
	cout << "HIGHEST DIGIT: " << highestDigit << endl;
	cout << "SIZE OF ARRAY: " << sizeof(binArr) << endl;
	binArr[7] = 125; cout << "BINARR 7: " << binArr[7] << endl;
	*/


	//conversion to binary
	while ((input >= 0) && (digit >= 0))
	{
		if ((input - subVal) < 0)
		{
			binArr[digit] = 0;
			digit -= 1;
			subVal /= 2;
			continue;
		}
		else if ((input - subVal) >= 0)
		{
			input -= subVal;
			binArr[digit] = 1;
			digit -= 1;
			subVal /= 2;
			continue;
		}

	}
	for (int i = 0; i <= (highestDigit-1); ++i) { cout << binArr[i]; }
	cout << endl;
	return "No Answer!";
}
string convertDecOcto(int input = 0)
{
	int dummyInput = input, iterations = 0, tempArr[100],octoArr[100];
	//figuring out the list of remainders
	//This needs to be reversed later
	while (dummyInput/8>0) {
		tempArr[iterations] = dummyInput%8;
		dummyInput = floor(dummyInput / 8);
		++iterations;
	}
	tempArr[iterations] = dummyInput % 8;

	//Displaying the final array
	for (int i = iterations; i >= 0; --i) { cout << tempArr[i]; }; cout << endl;

	return "No Answer";
}
string convertDecHex(int input = 0)
{
	//stupid definitions
	char zero = '0', one = '1', two = '2', three = '3', four = '4', five = '5', six = '6', seven = '7', eight = '8', nine = '9', ten = 'A', eleven = 'B', twelve = 'C', thirteen = 'D', fourteen = 'E', fifteen = 'F';
	char reference[16] = {zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen};
	string finalAns = "                                                 ";
	int iterations1=0,tempAns[100];
	int dummyInput = input;

	//figuring out remainders
	while (dummyInput / 16 > 0) {
		tempAns[iterations1] = dummyInput % 16;
		dummyInput = floor(dummyInput / 16);
		++iterations1;
	}
	tempAns[iterations1] = dummyInput % 16;

	//conversion to string
	//take every individual asset in tempAns, and plug the number into the reference array.
	for (int i = 0; i <= iterations1 ; ++i)
	{
		char currStringRef = reference[tempAns[i]];
		finalAns[i] = currStringRef;
	}
	for (int i = iterations1; i >= 0; --i) { cout << finalAns[i]; }; cout << endl;
	return "No Answer";
}
string convertBinDec(int input = 0)
{
	return "Unfinished :)";
}

int main() 
{
	while (1==1)
	{
		int input,choice=1;
		cout << "Please enter a number to be converted: "; cin >> input;
		do { cout << "Would you like \n(1) Binary to Decimal \n(2) Decimal to Binary \n(3) Decimal to hexadecimal\n(4) Decimal to Octodecimal" << endl; cin >> choice; } while (choice <= 1 && choice >= 4);
		
		string answer = "No answer!";
		if (choice == 1) {answer = convertBinDec(input); }
		else if (choice == 2) {answer = convertDecBin(input); }
		else if (choice == 3) { answer = convertDecHex(input); }
		else if (choice == 4) { answer = convertDecOcto(input); }
		//cout << answer << endl;
	}
}