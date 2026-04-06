//1) C++ program to input Student_ID, student nameand marks of three subjects(Physics, Chemistryand Information Technology)
//2) Calculate total Grades, Average, and Level of student.
//if (percentage >= 60)
//strcpy(level, "First");
//else if (percentage < 60 && percentage >= 48)
//	strcpy(level, "Second");
//else if (percentage < 48 && percentage >= 36)
//	strcpy(level, "Pass");
//else strcpy(level, "Fail");



#include <iostream>
using namespace std;
int main()
{
	string studentName,level;
	int studentID, gradePhysics, gradeChemistry, gradeInformationTech,total;
	double avg;
	cout << "What is your name? "; cin >> studentName;
	cout << "What is your ID? "; cin >> studentID;
	cout << "What is your physics grade? "; cin >> gradePhysics;
	cout << "What is your chemistry grade? "; cin >> gradeChemistry;
	cout << "What is your information tech grade? "; cin >> gradeInformationTech;
	total = (gradePhysics + gradeChemistry + gradeInformationTech); avg = total / 3;
	if (total >= 60){level = "First";}
	else if (total < 60 && total >= 48) { level = "Second"; }
	else if (total > 48 && total <= 36) { level = "Pass"; }
	else { level = "Fail"; }
	system("CLS");
	cout << "NAME: " << studentName << endl << "ID: " << studentID << endl << "--------------------" << endl << "PHYSICS GRADE: " << gradePhysics << endl << "CHEMISTRY GRADE: " << gradeChemistry << endl << "INFORMATION TECH GRADE: " << gradeInformationTech << endl << "--------------------" << endl << "TOTAL GRADE: " << total << endl << "FINAL GRADE: " << avg << endl << "LEVEL: " << level << endl;

}
