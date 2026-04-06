#include <iostream>
#include <cmath>
using namespace std;


int main() {

	double a, b, c, discriminant, root1, root2;
	string disctype, roottype;

	cout << "Input a:"; cin >> a; cout << endl;
	cout << "Input b:"; cin >> b; cout << endl;
	cout << "Input c:"; cin >> c; cout << endl;
	discriminant = pow(b, 2) - (4 * a * c);


	if(discriminant == 0){
		disctype = "Equal to Zero";
		roottype = "Real and equal";
		root1 = ((b * -1) / (2 * a));
		root2 = root1;
	}

	if(discriminant > 0){
		disctype = "Greater than Zero";
		roottype = "Real and different";
		root1 = (-b + sqrt(pow(b, 2) - (4 * a * c))) / (2 * a);
		root2 = (-b - sqrt(pow(b, 2) - (4 * a * c))) / (2 * a);
	}

	if(discriminant < 0) {
		disctype = "Less than Zero";
		roottype = "Complex and Different";
		root1 = ((b * -1) / (2 * a))+(-b + sqrt(pow(b, 2) - (4 * a * c))) / (2 * a);
		root2 = ((b * -1) / (2 * a))+(-b - sqrt(pow(b, 2) - (4 * a * c))) / (2 * a);
	}

	cout <<"The discriminant is "<<discriminant<<", which is "<<disctype<<endl;
	cout <<"The roots are "<<root1<<" and "<<root2<<", which are "<<roottype<<endl;

	return 0;

}