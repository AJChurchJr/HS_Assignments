#include <iostream>
using namespace std;
int dist(char a, char b)
{
    int ascii_a =int(a),ascii_b=int(b);
    int total=abs(ascii_a-ascii_b);
    //cout << ascii_a << "|" << ascii_b << endl; //commented debug code
    return total;
}
int main()
{
    string wordA,wordB,origA,origB;int differenceVal=0; //definitions

    cout << "Input one word: "; cin >> wordA; cout << "Input another word: "; cin >> wordB; //Taking inputs
    origA = wordA;origB=wordB;//defining originals


    //Deleting extra bits
    if (wordA.length() != wordB.length()){
        if (wordA.length()>wordB.length()){while(wordA.length() != wordB.length()){wordA.erase((wordA.length()-1));}}
        else if (wordA.length()>wordB.length()){while(wordA.length() != wordB.length()){wordB.erase((wordB.length()-1));}}
        cout << "Words were shortened." << endl;
    }

    //Calculating Difference
    while(wordA.length()!= 0||wordB.length()!=0)
    {
        //cout << wordA[(wordB.length()-1)] <<"|"<< wordB[(wordB.length()-1)] << endl;
        //cout << wordA.length()<< "|" << wordB.length() << endl;
        //cout << dist(wordA[(wordB.length()-1)],wordB[(wordB.length()-1)]) << endl;
        differenceVal+=dist(wordA[(wordB.length()-1)],wordB[(wordB.length()-1)]);
        wordA.erase((wordB.length()-1));wordB.erase((wordB.length()-1));
    }

    cout << "The difference is: " << differenceVal;

    return differenceVal;
}
