#Andrew Church
#Programming assignment 4
#Step 4
import os
import time
import sys
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return

adminpassword='12345'



#This is only called if EVERYTHING is valid. IF everything is valid, it will edit all of the files and add the new usernames and passwords to them.
def account_creation_confirmation(tempusername,temppassword):
    print("Writing account info to data.txt")
    with open("data.txt", "r+") as datafile:
        datafile.seek(0)
        datastring=datafile.readline()
        datadict=eval(datastring)
        datadict[tempusername]=temppassword
        datafile2=open("data.txt", "w")
        datafile2.close()
        datafile.seek(0)
        datafile.write(str(datadict))
    print("Writing account info to usernames.txt")
    with open('usernames.txt','r+') as username_checker:
        username_checker.write(tempusername)
        username_checker.write("\n")
    print("Writing account info to passwords.txt")
    with open("passwords.txt", "r+") as passwords:
        passwords.seek(0,2)
        passwords.write(temppassword) 
        passwords.write("\n")
    print("All done!")
    time.sleep(1)
def createaccount():
    cls()
    #Createaccount sets the user's input as a temporary username that it uses to set everything. The variable gets deleted after the fact.
    tempusername=input("What is your name?")
    with open("usernames.txt", "r+") as username_checker:
        #the program checks if tempusername is in the usernames file
        tempusername_with_n=tempusername+"\n"
        if tempusername_with_n in username_checker.read():
            print("That username is taken, please try again.")
            print("Access denied.")
            time.sleep(1)
            return
        elif tempusername=='':
            print("Username cannot be blank!")
            return
        else:
            #If the username is not there, it will tell you the username is valid and it will ask for a password, which it uses with the function passwordcreation.
            print("Valid username.")
            temppassword=passwordcreation()
            if temppassword==False:
                print("Access denied.")
                time.sleep(1)
                return
            else:
                account_creation_confirmation(tempusername,temppassword)
def passwordcreation():
    with open("passwords.txt", "r+") as passwords:
        print("What would you like your password to be?", end='')
        temppassword=input()
        if temppassword=='' or temppassword=='none':
            print("You are not allowed to have a blank password!")
            temppassword=False
            return temppassword
        print("Password created!")
        return temppassword





#Management room that clears text files for me.
def adminroom():
    while True:
        cls()
        print("ADMIN MENU:\n(1)PRINT ALL USERNAMES\n(2)PRINT ALL PASSWORDS\n(3)PRINT ALL DATA,\n(4)SCRUB,\n or exit?")
        choice=input()
        if choice=='1':
            with open('usernames.txt', 'r') as usernames:
                username_string=usernames.readlines()
                print(username_string)
                input("Press enter to continue.")
                continue
        elif choice=='2':
            with open('passwords.txt','r') as passwords:
                password_string=passwords.readlines()
                print(password_string)
                input("Press enter to continue.")
                continue
        elif choice=='3':
            with open('data.txt', 'r') as data:
                data_string=data.readline()
                print(data_string)
                input("Press enter to continue.")
                continue
        elif choice=='4':
            print("scrubbing usernames.")
            usernamesfile=open('usernames.txt','w')
            usernamesfile.close()
            print("scrubbing passwords")
            passwordsfile=open('passwords.txt','w')
            passwordsfile.close()
            print("scrubbing data.")
            datafile=open('data.txt','w')
            datafile.write("{}")
            datafile.close()
            print("Scrubbing completed!")
            time.sleep(1)
        elif choice=='exit':
            print('\n\n')
            break
    return





   
#This is the first part of logon. It checks if the username is correct, and then calls logon2 for the password part of things.
def logon():
    cls()
    print("Type your username:", end='')
    choice=input()
    choice_with_n=choice+"\n"
    with open('usernames.txt', 'r') as usernames:
        if choice_with_n in usernames:
            print("password:", end='')
            choice2=input()
            choice2_with_n=choice+"\n"
            #The value 'logon' is what dictates if you are allowed to enter or not. On top of that, logon2 will send your username and password back if the logon is true. This makes the code much more complicated.
            datapackage=logon2(choice,choice2)
            #The program returns a tuple called 'datapackage', which will be unpacked with a new function. If the length of datapackage is 1, it will give a different result than 3.
            #If there are 3 items in a tuple, it automatically indicates that you got the password right.
            return datapackage
        else:
            logon=False
            return logon
def logon2(username,password):
    with open('data.txt', 'r') as data:
        datastring=data.readline()
        datadict=eval(datastring)
        if datadict[username]==password:
            logon=True
            return(logon,username,password)
        else:
            logon=False
            return logon



#data_unpack will get a specific tuple value and return it. 
def data_unpack1(datapackage):
    correct_logon=datapackage[0]
def data_unpack2(datapackage):
    username=datapackage[1]
    return username
def data_unpack3(datapackage):
    password=datapackage[2]
    return password
def welcome(correct_logon,username,password):
    cls()
    print("Welcome, " + username)
    print("your password is:" + password)
    input("You have logged in successfully. That is the end of this program. Thank you for testing!")



#-----------------------------------------------------------------------------------------------------------------
#This asks what the user would like to do, and executes a specific function based off of said choice.
triesleft=3
while True:
    cls()
    #every time you exit to the menu, it checks how many times you have tried to log on. If your logon tries left hits 0, the program ends.
    if triesleft<=0:
        print("You have tried to log on too many times! Please try again later.")
        time.sleep(1)
        sys.exit()
    print(str(triesleft) + " logon attempts left")

    print("Hello, welcome to [Insert Social Media Here!] Would you like to:")
    print("(1)log on\n(2)make a new account\nor exit?")
    choice=input()
    if choice=="2":
        createaccount()
    elif choice=="1":
        datapackage=logon()
        if datapackage==False:
            print("Invalid login. Username or password was incorrect.")
            triesleft-=1
            time.sleep(1)
        #The next functions will unpack the datapackage.
        #There will be variables assigned for 
        else:
            correct_logon=data_unpack1(datapackage)
            username=data_unpack2(datapackage)
            password=data_unpack3(datapackage)
        #Broadcasts a little message for you if you logged in correctly.
            welcome(correct_logon,username,password)
    elif choice=='exit':
        sys.exit()
    elif choice=="admin":
        choice=input("What is the admin password?")
        if choice==adminpassword:
            adminroom()
    else:
        print("invalid input")
        time.sleep(1)
        continue
