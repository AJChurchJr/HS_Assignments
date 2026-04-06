//// C++ EXERCISES.cpp : This file contains the 'main' function. Program execution begins and ends there.
////
//
//#include <iostream>
//using namespace std;
////
//////QUESTION ONE
////int main()
////{
////	int n = 4, k = 2;
////
////	cout << n++ << endl;
////	cout << n << endl;
////
////	cout << n++ << endl;
////	cout << n << endl;
////
////	cout << -n << endl;
////	cout << n << endl;
////
////	cout << --n << endl;
////	cout << n << endl;
////
////	cout << n-- << endl;
////	cout << n << endl;
////
////	cout << n + k << endl;
////	cout << n << endl;
////	cout << k << endl;
////
////	cout << n << k << endl;
////
////	cout << n << endl;
////	cout << " " << n << endl;
////
////	cout << " n" << endl;
////	cout << "\n" << endl;
////
////	cout << " n * n = "; //CAREFUL!
////	cout << n * n << endl;
////	cout << 'n' << endl;
////
////	return 0;
////}
//
////QUESTION 2
////int main() {
////	int n = 3;
////	while (n >= 0)
////	{
////		cout << n * n << endl;
////		--n;
////	}
////	cout << n << endl;
////	while (n < 4)
////		cout << ++n << endl;
////	cout << n << endl;
////	while (n >= 0)
////		cout << (n /= 2) << endl;
////	return 0;
////}
//
////QUESTION THREE
////int main()
////{
////	int n;
////	cout << (n = 4) << endl;
////	cout << (n == 4) << endl;
////	cout << (n > 3) << endl;
////	cout << (n < 4) << endl;
////	cout << (n = 0) << endl;
////	cout << (n == 0) << endl;
////	cout << (n > 0) << endl;
////	cout << (n && 4) << endl;
////	cout << (n || 4) << endl;
////	cout << (!n) << endl;
////	return 0;
////}
//
//////QUESTION SIX
////int main() {
////	int found = 0, count = 5;
////	if (!found || --count == 0)
////		cout << "danger" << endl;
////	cout << "count = " << count << endl;
////}
//
////QUESTION SEVEN
////int main()
////{
////	char ch;
////	char title[] = "Titanic";
////	ch = title[1];
////	title[3] = ch;
////	cout << title << endl;
////	cout << ch << endl;
////}
//
////QUESTION EIGHT
////int main()
////{
////	const int LENGTH = 21;
////	char message[LENGTH];
////	cout << "Enter a sentence on the line below." << endl;
////	cin >> message;
////	cout << message << endl;
////}
//
////QUESTION NINE
////int main()
////{
////	const int LENGTH = 21;
////	char message[LENGTH];
////	cout << "Enter a sentence on the line below." << endl;
////	cin.getline(message, LENGTH, '\n');
////	cout << message << endl;
////	return 0;
////}
//
////QUESTION TEN
////int main()
////{
////	const int LENGTH = 21;
////	char message[LENGTH];
////	cout << "Enter a sentence on the line below." << endl;
////	int i = 0;
////	do
////	{
////		cin.get(message[i]);
////		++i;
////	} 
////	while (i < LENGTH - 1 && message[i] != '\n');
////	
////	message[i] = '\0'; // Terminate string with NUL char.
////	cout << message << endl;////
////}
//
////QUESTION TWELVE
////int main() {
////	int n = 10;
////	while (n > 0){
////		n /= 2;
////		cout << (n *= n) << endl;	
////	}
////	
////}
//
////QUESTION 17
////int main(){
////	int n;
////	int k = 5;
////	n = (100 % k ? k + 1 : k - 1);
////	cout << "n = " << n << " k = " << k << endl;////}//////QUESTION 18//int main()//{
//	double x = 3.8;
//	int n = x;
//	cout << "n = " << n << endl;
//};

//POINTERS AND REFERENCES
#include <iostream>
using namespace std;
//
//int main() {
//	int* var;
//	int var2 = 5;
//	var = &var2;
//	cout << var;
//	return 0;
//}
int main() {
	int* pointer;
	int var = 3;
	pointer = &var;
	cout << pointer << endl;
	delete pointer;
	cout << var << endl;
}