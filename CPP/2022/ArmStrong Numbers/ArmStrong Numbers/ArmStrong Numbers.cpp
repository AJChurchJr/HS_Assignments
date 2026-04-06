//Credit to Andrew Church

#include <iostream>
#include <cmath>
using namespace std;


bool isArmstrong(int inputNum = 123) 
{

	int inputArray[3];int outputNum=0;

	
	int cycles = 2, numCopy = inputNum; while (numCopy > 0){inputArray[cycles] = numCopy % 10; numCopy /= 10;--cycles;} // Credit to iceCrime on stackoverflow -- divides number into individual digits
	if (inputNum < 100) { inputArray[0] = 0; }; if (inputNum < 10) { inputArray[0] = 0; inputArray[1] = 0; }

	for (int i = 0; i <= 2; i++) 
	{outputNum += pow(inputArray[i], 3);}
	//cout << inputNum << "||" << outputNum << endl;
	if (inputNum == outputNum) { return true; }
	else { return false; }

}

int main()
{
	int inputNum = 0;
	do { cout << "Please input a THREE-DIGIT number: "; cin >> inputNum; } while ((inputNum / 1000 >= 1));
	bool armstrong = isArmstrong(inputNum);
	if (armstrong == 1) { cout << "Your number is an armstrong number!" << endl; }else { cout << "Your number is NOT an armstrong number!" << endl; } cout << endl;
	

	cout << "List of valid armstrong numbers:\n------------------------------" << endl;
	for (int i = 0; i <= 999; ++i)
	{
		if (isArmstrong(i)) {cout << i << endl;}
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
