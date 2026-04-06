//1.1
//it uses a naming convention; a noun that is gramatically correct

//1.2 
int mainbutnegative()
{
    return -1;
}

//1.3
#include <iostream>
int helloworld()
{
    std::cout << "Hello World" << std::endl;
    return 0;
}

//1.4
#include <iostream>
int multiply()
{
    int v1=0,v2=0;
    std::cin >> v1 >> v2;
    std::cout << "The product of " << v1 << " and " << v2 << " is " << v1*v2 << std::endl;
}

//1.5 
#include <iostream>
int smallbitmultiply()
{
    int v1=0,v2=0;
    std::cin >> v1 >> v2;
    std::cout << "The product of " << std::endl;
    std::cout << v1 << " and " << v2 << std::endl; 
    std::cout << "is " << v1*v2 << std::endl;
}

//1.6
/*
The following code is NOT legal because the program uses semicolons as if it is fully finishing A statement when it is not. The statement remains unfinished without endl several times.
You can fix this issue by removing the semicolons and putting it all back on one line. 
*/


//1.7
//* hey
//* look at me
//* i am incorrectly nested
//* i am horribly unoptimized 

//1.8
#include <iostream> 
int commentdisplay()
{
    std::cout << "*/";
    return 0 ;
}
//option 2 is legal

//1.9: 
#include <iostream> 
int fiftytohundred() 
{
    int num = 0; //defines num 
    while (num < 100) //repeats until num is equal to or greater than 100 
    {
        ++num; //adds 1 to num 
        if (num >= 50) //displays the number while it's greater than 50 
        {
            std::cout << num << std::endl; 
        }
    }
}

//1.10
#include <iostream> 
int tentozero() 
{
    int num = 100; //defines num 
    while (num > 0) //repeats until num is less than 0 
    {
        --num; //subtracts from num 
        if (num <= 10) //displays the number while it's less than 10 
        {
            std::cout << num << std::endl; 
        }
    }
}


//1.11
#include <iostream>
int minmax()
{
    int min = 0, max = 0;
    std::cin >> min >> max; //takes input for min and max
    int currentnum = min; //defines currentnum to min 
    while (currentnum < max) //repeats until currentnum is greater than the max
    {
        currentnum += 1;
        std::cout << currentnum << std::endl; //adds 1 to currentnum and diaplays it
    }
    return 0;
}

//1.12 
//The for-loop adds i to sum while i is less than 100. 
//The final value would end up being 0
int ihundred()
{
    int sum = 0;
    for (int i = -100; i <= 100; ++i)
        sum += i;
    std::cout << sum << std::endl;
    return 0;
}

//1.13
//for loops are nice but the question of 1.4 is simple addition and subtraction

//1.14
//FOR loops are meant to stop eventually. A value is defined and a condition is pre-applied and begun. 
//WHILE loops have no intention to stop unless their condition is met through outsider means. 

//1.15
//error: missing ) in paramater list for main
/*
int main()
{
    std::cout << "Read each file." << std::endl;
    std::cout << Update master. << std::endl;
    std::cout << "Write new master." << std::endl;
    return 0;
}
*/

//1.16
#include <iostream> 
int sumThree()
{
    int v1 = 0, v2 = 0, v3 = 0;
    std::cout << "Enter three numbers, separated by spaces: ";
    std::cin >> v1 >> v2 >> v3;
    std::cout << "The sum of " << v1 << ", " << v2 << ", and " << v3 << " is " << v1+v2+v3 << std::endl;
    return 0; 

}

//1.17-1.18
//If the same numbers are input over and over again, nothing will display, because it waits for a different number to be input in order to actually display anything. It creats an endless, unbreakable loop that will never finish. 
//If different numbers are input every time, there will never be any buildup of numbers, and the output will always be "[x] occured 1 time"


//1.19 -- 1.4.1 code again 
int main(){
    int sum = 0;
    //values 1 through 10 inclusive
    for (int val = 1; val <= 10; ++val)
        sum += val; //equivalent to sum = sum + val
    std::cout << "Sum of 1 to 10 inclusive is: " << sum << std::endl;
    return 0;
}
