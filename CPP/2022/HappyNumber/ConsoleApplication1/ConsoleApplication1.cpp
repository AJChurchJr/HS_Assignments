//Programming by Andrew Church
/* DOCUMENTATION
0. start with input number X
1. take number X, split it into array (keep note of digits)
2. for every number in the array (this is why you need to keep note of digits):
	- square said number
	- add them to create new number X
3. IF new number X is 0:
	- complete with answer YES
   ELSE:
	- fall back to step 1 with new number X
*/
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	int inputNum, inputArray[3], checkLimit, attempts = 1;
	cout << "Please input a THREE-DIGIT number: "; cin >> inputNum;cout << "How long would you wish to check?: "; cin >> checkLimit;
	while (inputNum != 1) {

		//ICECRIME ON STACKFLOW CREATED THIS -- DIVIDES NUMBER INTO DIGITS
		int cycles = 2, numCopy = inputNum; while (numCopy > 0) { 
			inputArray[cycles] = numCopy % 10; 
			numCopy /= 10; --cycles; 
		}
		
		if (inputNum < 100) { inputArray[0] = 0; }; //Emergency inputs in case digits become less than 3 -- fills in with 0
		if (inputNum < 10) { inputArray[0] = 0; inputArray[1] = 0; } //Emergency inputs in case digits become less than 3 -- fills in with 0

		inputNum = 0; //resets inputNum for addition later

		cout << "NUMBERS FOR ATTEMPT " << attempts << ": " << inputArray[0] << "|" << inputArray[1] << "|" << inputArray[2] << endl; //debug print

		for (int i = 0; i <= 2; i++) {
			inputArray[i] = inputArray[i] * inputArray[i]; 
			inputNum += inputArray[i]; } //squaring numbers and adding them to the new number

		cout << "NUMBERS AFTER SQUARE: " << inputArray[0] << "|" << inputArray[1] << "|" << inputArray[2] << endl; cout << "NUMBERS AFTER ADDING: " << inputNum << endl;//debug print
		
		attempts++; checkLimit--; //updating values for debug prints and giving up.
		
		if (inputNum == 1) { cout << "Number is happy | completed in " << attempts << " moves."; return 1; }
		
		else if (checkLimit <= 0) { cout << "Number is not happy."; return 0; } //user prints 
	}
}

