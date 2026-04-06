#ifndef ACCOUNT_HPP
#define ACCOUNT_HPP
#include <vector>
#include <map> 

class Account {

public:


  // variables.
  double balance = 0.0;
  bool initialized = false;
  std::vector<std::string> statement = {};
  std::string address, passwd, city, state ;


  // depositing is easy because it just adds an amount and doesn't have to check
  // for much
  bool deposit(double amount) {
    balance += amount;
    state_upd("Deposit", amount);
    return true;
  }


  // for withdrawing, it has to make sure there is enough to withdraw
  bool withdraw(double amount) {
    if (balance > amount) {
      // if there is enough, it withdraws and says it was a success
      balance -= amount;
      state_upd("Withdraw", amount);
      return true;
    } else {
      // if not, it says something went wrong
      return false;
    }
  }

    

  // For actually importing all the data
  void initialize(std::string _account, std::string _SSN, std::string _name,
                  std::string _address, std::string _city, std::string _state,
                  std::string _passwd, std::string _linked_account,
                  std::string _account_type = "checking", long double _balance = 0.0) {
    account = _account;
    SSN = _SSN;
    name = _name;
    address = _address;
    city = _city;
    state = _state;
    passwd = _passwd;
    linked_account = _linked_account;
    account_type = _account_type;
    balance = _balance;
    initialized = true;
  }

  bool save_to_file() {
    // This function saves the individual account to a file
    // Do not use this
    // checking to see if the account is initialized
    if (initialized != true) {
      return false;
    }

    // file pointer
    std::fstream fout;
    // opens an existing csv file or creates a new file.
    fout.open("accounts.csv", std::ios::out | std::ios::app);

    // Outputting current information to file
    fout << account << "," << SSN << "," << name << "," << address << ","
         << city << "," << state << "," << passwd << "," << linked_account
         << "," << account_type << "," << balance << "\n";

    return true;
  }



    std::map<std::string,std::vector<std::string>> save_to_map( std::map<std::string,std::vector<std::string>> map ) {
      map[account] = {SSN,name,address,city,state,passwd,linked_account,account_type,std::to_string(balance)};
      return map;
    }
    
    //Parses a string (in a way) to return a version of that string with only a certain amount of characters visible
    //word is the string that is being parsed, digits is how many characters at the end of the string will be visible.
    std::string parse(std::string word, int digits){
      std::string parsed = "";
      //For loop that iterates for however long the word is.
      for (int i = 0; i < word.size(); ++i){
        //If the code would refer to a character (using i) that is not desired to be displayed, an asterisk is added to the parsed string.
        if (i < (word.size() - digits)){
          parsed += "*";
        }
          //Other wise, the character refered to is added to the parsed string.
        else{
          parsed += word[i];
        }
      }
      //Returns the parsed string.
      return parsed;
    }


  // Displaying the account balance and other important information.
  void inquiry() {
    if (initialized != true) {
        std::cout << "Failed.";
        return;
    }
    std::cout << "\n\n" << account_type << " Account Details" << std::endl;
    std::cout << "Name: " << name << std::endl;
    std::cout << "Account number: " << account << std::endl;
    std::cout << "Address City State: " << address << ", " << city << ", "
              << state << std::endl;
    // remember to eventually splice the SSN to have only the last 4 digits
    std::cout << "Social Security: " << parse(SSN, 4) << std::endl;
    std::cout << "Balance: $" << balance << std::endl;
  }



  //Function for the monthly statement. Put at the end of any transaction function, before the return statment, for easily updating the monthly statement.
  //"transaction" is the type of transaction as a string, "amount" is the amount of money involved in that transaction.
  void state_upd(std::string transaction, long double amount){
    statement.push_back(transaction + " of $" + std::to_string(amount));
  }



    //Function to print the monthly statement. IDK WHERE WE WANT TO PUT THIS
    void print_state(){
    for (int i = 0; i < statement.size(); ++i){
      std::cout << (i + 1) << ". " << statement[i] << std::endl;
    }
  }

private:
    // values that are not needed to be changed like ever lol
    std::string account, SSN, name;
    // savings/checking account differentiation 
    std::string account_type = "checking"; 
    std::string linked_account;
};

#endif


/*
//Saving the monthly statement to its own file. The file name uses the account number for easy reference.
  //If we need to we could probably have this in the same file as the account info later.
  bool save_statement(){
    //idk if this needs to be here
    if (initialized != true) {
      return false;
    }
    //File pointer
    std::fstream fout;
    //Opens or creates the specified csv file.
    fout.open((account + "mst.csv"), std::ios::out | std::ios::app);
    //Outputting the monthly statement to the file
    for (int i = 0; i < statement.size(); ++i){
      fout << statement[i];
      //Makes sure no extra comma is added to the end of the file line.
      if ((i+1) < statement.size()){
        fout << ",";
      }
    }
    fout << "\n";
    return true;
  }
*/



/*
bool transfer(double amount, Account& other_acc){
        if (withdraw(amount)){
            other_acc.deposit(amount);
            state_upd(("Transfer (" << account_type << " -> " << other_acc.account_type), amount);
            return true;
        }
        else{
            return false;
        }
    }


*/