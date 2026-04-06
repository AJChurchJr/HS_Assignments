/* CREDITS
- account.hpp: ANDREW CHURCH
- converting menu to class: ANDREW CHURCH
- menu system: KEEGAN WILLS, JAYMIA STARK
- Saving the program: RYAN JEAN
*/

#include <cmath>
#include <cstdlib>
#include <fstream>     
#include <iostream>
#include <sstream>
#include <vector>
#include <map>       
#include <any>
#include <string>
#include "account.hpp"




class Menu {
    public:


        void update() {
            std::cout << "\n\n###----------------";
            switch(current_menu) {
                case 0:
                    std::cout << "START MENU " <<std::endl;
                    startmenu();
                    break;
                case 1:
                    std::cout << "CREATE ACCOUNT " <<std::endl;
                    create();
                    break;
                case 2:
                    std::cout << "LOGIN MENU " <<std::endl;
                    login();
                    break;
                case 3:
                    std::cout << "MAIN MENU " <<std::endl;
                    mainmenu();
                    break;

            }

        }



        void startmenu() {

            //-------- ASKING TO LOG IN OR CREATE AN ACCOUNT
            std::cout << "Would you like to \n(1) LOG IN?\n(2) CREATE ACCOUNT?\n(3) DISPLAY ALL ACCOUNTS (DEBUG)\n>";
            std::cin>>current_option;
            switch(current_option){
                case '1':
                    current_menu = 2;
                    break;
                case '2':
                    current_menu = 1; 
                    break;
                default:
                    for (auto i=loaded.begin() ; i!=loaded.end() ; i++) {std::cout << i->first << ": " << loaded[i->first][1] << std::endl;}

                    break;
            }

        }



        void create() {

            //------- THE PROCESS OF CREATING AN ACCOUNT
            std::cout << "!!!IMPORTANT NOTE, DO NOT USE SPACES! USE UNDERSCORES (_), SPACES WILL BREAK THE PROGRAM!!!\n";
            std::cout << "What is your SSN:"; std::cin >> create_vals[0];
            std::cout << "What is your full name: "; std::cin >> create_vals[1];
            std::cout << "What is your address: "; std::cin >> create_vals[2];
            std::cout << "What is your city: "; std::cin >> create_vals[3];
            std::cout << "What is your state initials: "; std::cin >> create_vals[4];
            std::cout << "What is your password: "; std::cin >> create_vals[5];

            // Creating two new account numbers
            create_check = gen_num(10);
            create_save = gen_num(10);

            // Adding checkings and savings information to the loaded list
            loaded[create_check] = {create_vals[0],create_vals[1],create_vals[2],create_vals[3],create_vals[4],create_vals[5],create_save,"checking","0.00"};
                loaded[create_save] = {create_vals[0],create_vals[1],create_vals[2],create_vals[3],create_vals[4],create_vals[5],create_check,"savings","10.00"};

            //output
            std::cout << "\nAccount created. $10.00 added to your savings as a sign-up bonus.\nYour account number is [" << create_check << "] and your savings number is [" << create_save << "]. Thank you!\n";

        //passing new account through as login credentials
        username_input = create_check; 
        current_menu = 3;
        initialize();
        }




        void login() {

            //it do attempts now
            while (attempts < 5) {

                //taking input as a login attempt
                attempts ++;
                std::cout << "---ATTEMPT " << attempts << std::endl;
                std::cout << "Enter account number: "; std::cin >> username_input;
                std::cout << "Enter password: "; std::cin >> password_input;


                // iterating through the keys of the map, to see if the username is a match anywhere
                for (auto i=loaded.begin() ; i!=loaded.end() ; i++) {
                    //checking to see if the username matches
                    if (username_input == i->first) {
                        //if the right password is found
                        if (password_input == loaded[username_input][5]) {success = true;break;}
                        //if the username is right but the password is wrong
                        else {success = false;break;}
                    }}


                //if the credentials are wrong, it kicks you out.
                if (not success) {std::cout << "Username or password incorrect.\n";continue;}
                else if (success) {std::cout << "Welcome, " << loaded[username_input][1] << "!\n"; break; }
            }

            //after the attempts are over, checking for success or not
            if (success) {initialize();current_menu = 3; }
            else {current_menu = 0;}
        }



        void initialize() {
            //--------LOGGING IN USING CREDENTIALS
            linked_acc = loaded[username_input][6];
            if (loaded[username_input][7] == "checking"){
            checking.initialize(username_input,loaded[username_input][0],loaded[username_input][1],loaded[username_input][2],loaded[username_input][3],loaded[username_input][4],loaded[username_input][5],loaded[username_input][6],loaded[username_input][7],std::stod(loaded[username_input][8]));
            savings.initialize(linked_acc,loaded[linked_acc][0],loaded[linked_acc][1],loaded[linked_acc][2],loaded[linked_acc][3],loaded[linked_acc][4],loaded[linked_acc][5],loaded[linked_acc][6],loaded[linked_acc][7],std::stod(loaded[linked_acc][8]));
            }
            else if (loaded[username_input][7] == "savings"){
                savings.initialize(username_input,loaded[username_input][0],loaded[username_input][1],loaded[username_input][2],loaded[username_input][3],loaded[username_input][4],loaded[username_input][5],loaded[username_input][6],loaded[username_input][7],std::stod(loaded[username_input][8]));
                checking.initialize(linked_acc,loaded[linked_acc][0],loaded[linked_acc][1],loaded[linked_acc][2],loaded[linked_acc][3],loaded[linked_acc][4],loaded[linked_acc][5],loaded[linked_acc][6],loaded[linked_acc][7],std::stod(loaded[linked_acc][8]));
            }
        }




        void mainmenu() {
            std::cout << "Would you like to: " << "\n(1) - Deposit money." << "\n(2) - Withdraw money." << "\n(3) - Transfer Money to savings." << "\n(4) - Change address." << "\n(5) - Change Password."<< "\n(6) - Save progress." << "\n(7) - Inquire." << "\n(8) - Log out (and save).\n> "; std::cin >> current_option;


            switch(current_option){
                //depositing money (handled in account class)
                case '1':
                    std::cout << "Deposit amount: $"; std::cin >> modifier1;
                    output = checking.deposit(modifier1);
                    if (output == true){std::cout << "Successfully deposited $" << modifier1 << std::endl;}
                    break;


                //withdrawing money (handled in account class)
                case '2':
                    std::cout << "Withdraw amount: $"; std::cin >> modifier1;
                    output = checking.withdraw(modifier1);
                    if (output == true){std::cout << "Successfully withdrawn $" << modifier1 << std::endl;}
                    else {std::cout << "Withdraw unsuccessful. You may not have enough funds.\n";}
                    break;


                //transferring money to savings (handled here) 
                case '3':
                    std::cout << "Transfer amount: $"; std::cin >> modifier1;
                    output = checking.withdraw(modifier1);
                    if (output == true) { std::cout << "Transferring..."; }
                    else { std::cout << "Not enough money to transfer.\n"; break;}
                    output = savings.deposit(modifier1);
                    if (output == true) { std::cout << "Successful!";}
                    break;


                //changing address directly
                case '4':
                    std::cout << "Would you like to change:\n(1) - Address\n(2) - City\n(3) - State\n>"; std::cin >> current_option2;
                    switch(current_option2){
                        case '1':
                            std::cout << "New address (NO SPACES, use UNDERSCORES): "; 
                            std::cin >> checking.address;
                            break;
                        case '2':
                            std::cout << "New City (NO SPACES, use UNDERSCORES): ";
                            std::cin >> checking.city;
                            break;
                        case '3':
                            std::cout << "New state (NO SPACES, use UNDERSCORES): ";
                            std::cin >> checking.state;
                            break;
                    }
                    std::cout << "...changed!\n";
                    break;


                //changing password directly
                case '5':
                    std::cout << "New password (NO SPACES): "; std::cin >> checking.passwd;
                    std::cout << "...changed!\n";
                    break; 


                case '6':
                    loaded = checking.save_to_map(loaded);
                    break; 


                case '7':
                    std::cout << "Inquire about:\n(1) - Checkings\n(2) - Savings\n"; std::cin >> current_option2;
                    switch(current_option2){
                        case '1':
                            checking.inquiry();
                            break;
                        case '2':
                            savings.inquiry();
                            break;
                        default:
                            std::cout << "err ";
                            break;
                    }
                    break;


                default:
                    break;}
            if (current_option == '8') {loaded = checking.save_to_map(loaded);current_menu = 0;}
        }



        std::string gen_num(int length) {
            //For generating the account number. | Needs <cmath> <string> maybe <cstdlib> | Made by Keegan Wills
            //CHANGES: acc_num now starts off as a string, and just has the randomized digits converted to a string right away and then added to acc_num. length determines how many digits
                //Seed for the random number
                srand((unsigned) time(NULL));
                //Initializing account number
                std::string acc_num = "";
                //This for loop provides 10 random numbers, and adds them to become a 10 digit number.
                for (long int i = 0; i < length; ++i){
                //Adds a randomized digit to account number
                acc_num += std::to_string(1 + (rand() % 9));
                }
                return acc_num;
            }

    private:
        //-------- VARIABLE NAMES
        // Creating an account for test purposes
        Account checking, savings;
        // Login values
        std::string username_input,password_input,linked_acc; bool success = false; int attempts = 0; 
        //Menu option values
        char current_option,current_option2;  // the current choice made for the option menu
        double modifier1 = 0.0; // a 'modifier', a basic input used for the money stuff. used for deposit, withdraw, transfer, etc. 
        bool output = false; // an output variable saying if the transfer was a success or not
        //Create account values
        std::string create_check,create_save; 
        std::vector<std::string> create_vals = {"...","...","...","...","...","...","...","...","..."};
        //--------HOLDER FOR ALL ACCOUNTS 
        std::map<std::string,std::vector<std::string>> loaded;

        //-------- MENU VARIABLES
        int current_menu = 0; //0 -> login or create account? ; 1 -> create account ; 2 -> log in ; 3 -> main menu stuff


};





// std::string to_string();
// std::stod();



int main() {
    Menu menu;
    //STARTING THE MAIN MENU ONCE LOGGED IN
    while (true) {
        menu.update();
        } 
    /* WHAT IS WHAT in a vector?
    key: account num
    value[0]: SSN
    value[1]: name
    value[2]: address
    value[3]: city
    value[4]: state
    value[5]: password
    value[6]: linked account
    value[7]: account type (checking or saving)
    value[8]: balance (needs to be converted with std::stod();)
    */   
}
