#CREATED BY ANDREW CHURCH.
#2/26/2021
#I know people who change code are probably gonna delete this but I worked hard on this piece of crap. Please be nice :((


#--------------------------------------------------------------------------
#IMPORTS
import time
import sys
import os
import pickle
import gzip


#---------------------------------------------------------------------------
#EASE OF ACCESS FUNCTIONS
#THESE FUNCTIONS ARE SIMPLE FUNCTIONS USED TO MAKE MY LIFE EASIER, OR FOR EXTRA PIZAZZ.

#CHECK DIAGNOSTICS
#This will check and see if any files are missing important data.
def diagnostics():
    print("THIS IS THE STARTUP DIAGNOSTICS FUNCTION. THIS WILL CHECK FOR IMPORTANT DATA THAT IS NEEDED TO MAKE THE PROGRAM FUNCTION.")
    time.sleep(3)
    print("CHECKING masterpass.gz...")
    try:
        with gzip.open("masterpass.gz","r") as masterpass:
            print(masterpass)
            print("MASTERPASS.GZ IS FOUND.")
    except:
        print("MASTERPASS IS NOT FOUND. PROGRAM CANNOT START.")
        time.sleep(1)
        sys.exit()
    else:
        pass
    time.sleep(0.3)
    print("SUCCESS.")
    time.sleep(0.3)
    print("CHECKING data.gz...")
    time.sleep(0.3)
    try:
        with gzip.open("data.gz","r") as data:
            print(data)
            print("DATA.GZ FOUND.")
    except:
        print("DATA IS NOT FOUND. PROGRAM CANNOT START.")
        time.sleep(1)
        sys.exit()
    else:
        pass
    time.sleep(0.3)
    print("SUCCESS.")
    time.sleep(0.3)
    print("ATTEMPTING TO OPEN masterpass.gz...")
    time.sleep(0.3)
    try:
        with gzip.open("masterpass.gz","r") as test:
            var=test.readline()
            var=gzip.decompress(var)
            var=pickle.loads(var)
            print("PASSWORD FOUND. NO ERRORS.")
    except:
        print("ERROR.")









#This is a function used for when you need admin permission.
def adminpermission():
    with gzip.open('masterpass.gz','r') as masterpass:
        variable=masterpass.readline()
        variable=gzip.decompress(variable)
        variable=pickle.loads(variable)
    printf("This requires admin permissions, please enter your MASTER PASSWORD to continue:", end=='')
    attempt=input()
    if attempt==variable:
        printf("Correct.")
        value=True
        return value
    else:
        printf("Incorrect.")
        value=False
        return value




    
    


#printf is a message that makes text autoscroll
def printf(message, *word, end = "\n", sep = " "):
    for letter in message:
        print(letter, end = '', flush = True)
        time.sleep(0.01)
    if word:
        for letter in word:
            print(letter, end = '', flush = True)
            time.sleep(0.05)
    else:
        pass
    if end == '':
        pass
    else:
        print("\n", end = '')
    return







#This is a program that clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return








#CHECK FOR LENGTH
#Check for length will notify you if your program is empty, to prevent an error.
def check_for_length(saved_data):
    if len(saved_data)==0:
        printf("You have no accounts!")
        printf("Press enter to exit.", end='')
        input()
        length=0
        return length








#This will open the data.txt file and save the entirety of it a string, then a dictionary. This will be used later.
def savefile():
        with gzip.open('data.gz', 'r') as data:
            #FOR ALL THINGS CONCERNING GZIP.
            #WHAT GZIP DOES IS DECOMPRESS AND COMPRESS DATA. IF YOU ARE INTERESTED, CHECK THE PICKLER.PY
            saved_data=data.readline()
            saved_data=gzip.decompress(saved_data)
            saved_data=pickle.loads(saved_data)
            saved_data=str(saved_data)                        
            saved_data=eval(saved_data)
            return saved_data








#This is a program that checks the length of your program after it is saved as saved_data.
def checklength(saved_data):
    if len(saved_data)==0:
        printf("You have no accounts!")
        printf("Press enter to exit.", end='')
        input()
        return
    else:
        return






    
#This is a simple little thing that asks for the MASTER PASSWORD before you can access your other junk. The only problem with this is that I can't hide the master password so I have to put it directly in the code for now
def passwordverify():
    with gzip.open('masterpass.gz','r') as masterpass:
        variable=masterpass.readline()
        variable=gzip.decompress(variable)
        variable=pickle.loads(variable)
    printf("*Welcome to your digital password keeper, please enter your password to continue: ", end='')
    choice=input()
    #If the password is correct, it continues. If the password is incorrect, the program closes out.
    if choice==variable:
        print("*Password correct.")
        time.sleep(0.5)
        return
    else:
        sys.exit()





        
#-------------------------------------------------------------------------------
#IMPORTANT FUNCTIONS
#FUNCTIONS LIKE THIS ARE WHAT MAKES UP A GOOD 90% OF THE CODE. IT USES A LOT OF THE EASE-OF-ACCESS FUNCTIONS.


#MAINMENU
#Once you get the password right, it opens the Main Menu
#This simply asks if you wanna read your passwords or print them\
#The code will run a checker that checks the length of data.txt in order to tell if the program will run right or not. If the length is 0 it will not run.
def MainMenu():
    while True:
        cls()
        printf("*READ\n*ADD\n*SEARCH\n*DELETE\n*EDIT\n*SETTINGS\n*CLOSE")
        choice=input()
        if choice.lower()=='read':
            saved_data=savefile()
            length=check_for_length(saved_data)
            if length==0:
                continue
            readdata()
        elif choice.lower()=='add':
            adddata()
        elif choice.lower()=='search':
            saved_data=savefile()
            length=check_for_length(saved_data)
            if length==0:
                continue
            search()
        elif choice.lower()=='delete':
            saved_data=savefile()
            length=check_for_length(saved_data)
            if length==0:
                continue
            delete()
        elif choice.lower()=='edit':
            saved_data=savefile()
            length=check_for_length(saved_data)
            if length==0:
                continue
            edit()
        elif choice.lower()=='settings':
            settings()
        elif choice.lower()=='close':
            sys.exit()
        else:
            printf("Please put in a valid input.")

#READDATA
#This is a program that prints the entire data.txt file
#It opens the file, then uses the .keys() module in order to print the keys and values.
#The key is the name of the site, then the value is the user and password stored in a list
def readdata():
    cls()
    saved_data=savefile()
    for key,value in saved_data.items():
        printf(key + "" + "\nUsername: " + value[0] + "\nPassword: " + value[1] + '\n')
    time.sleep(1)
    input("Press enter to close.")
    return

#ADDDATA   
#This is a program that allows you to add new passwords. It will ask for a username, then a password, and then what site it is for.
#The site name will be registered as the key, and then the username and password will be registered as a list in the value.
#This is how it is read in the print message.
def adddata():
    saved_data=savefile()
    cls()
    printf("Please enter your new username:", end='')
    temp_user=input()
    printf("Please enter your new password:", end='')
    temp_password=input()
    printf("What site is this account for? ", end='')
    temp_site=input()
    #Temp_site will then be put through the dictionary to check if there is already a key under the same name there. If there is, it will ask for another one.
    while True:
        if temp_site in saved_data:
            printf("This site already has a saved account on it. (If it is an alt, add the word alt to the end or give another way to specify.) Would you like to rename it? ", end='')
            choice=input()
            if choice.lower()=='no' or choice.lower()=='n':
                del choice
                return
            if choice.lower()=='yes' or choice.lower()=='y':
                del choice
                printf("Name your new site:",end='')
                temp_site=input()
                continue
        else:
            break
    #This code, instead of appending, will copy the entire document, delete the original, and then paste the new one over it. 
    print("Saving data... Do not turn off...")
    saved_data[temp_site]=[str(temp_user),str(temp_password)]
    
    #this gzip code will either compress or decompress the code, and then write the compressed code or read the decompressed code
    with gzip.open('data.gz', 'w') as data:
        saved_data=pickle.dumps(saved_data)
        saved_data=gzip.compress(saved_data)
        data.write(bytes(saved_data))

#SEARCH
#Search will search for a specific keyword in every key, value[0], and value[1], and print everything.
def search():
    cls()
    saved_data=savefile()    
    #This code will search for a specific key in the dictionary, and then will prints it.
    printf("Please search for the account you would like to delete.",end='')
    search=input()
    if search.lower()=='close':
        return
    printf("Searching for accounts...")
    counter=0
    #This is probably going to be a big, confusing blob of code.
    #What this does is takes each key that matches the search in and assigns it to a number value.
    #It will then remove the key that is equivalent to that number value.
    results={}
    loopcount=0
    #%s will basically add a value to the end of a key. 
    #That value changes each time it loops so you can select whatever you want. 
    #Dear god this was complicated
    for key,value in saved_data.items():
        if search in key:
            loopcount+=1
            results["choice%s" %loopcount]=[key,value[0],value[1]]
            continue
        if search in value[0]:
            loopcount+=1
            results["choice%s" %loopcount]=[key,value[0],value[1]]
            continue
        if search in value[1]:
            loopcount+=1
            results["choice%s" %loopcount]=[key,value[0],value[1]]
            continue  
    if loopcount==0 or loopcount<0:
        printf("There were no results found.")
        printf("Press enter to return.")
        input()
        return
    printf("There were " + str(loopcount) + " results found.")
    for key,value in results.items():
        printf(key + ":" + value[0] + "   username: " + value[1] + "   password: " + value[2] )    


#DELETE
#DELETE IS COPIED FROM SEARCH.
#Delete will ask for a keyword, and then, like search, will show all the related items, but you can only search by the website, aka the key.
def delete():
    cls()
    saved_data=savefile()    
    #This code will search for a specific key in the dictionary, and then will overwrite it.
    printf("Please search for the account you would like to delete.",end='')
    deletechoice=input()
    if deletechoice.lower()=='close':
        return
    printf("Searching for accounts...")
    counter=0
    #This is probably going to be a big, confusing blob of code.
    #What this does is takes each key that matches the search in and assigns it to a number value.
    #It will then remove the key that is equivalent to that number value.
    delete_selection={}
    loopcount=0
    #%s will basically add a value to the end of a key. 
    #That value changes each time it loops so you can select whatever you want. 
    #Dear god this was complicated
    for key,value in saved_data.items():
        if deletechoice in key:
            loopcount+=1
            delete_selection["choice%s" %loopcount]=key
            continue
        if deletechoice in value[0]:
            loopcount+=1
            delete_selection["choice%s" %loopcount]=key
            continue
        if deletechoice in value[1]:
            loopcount+=1
            delete_selection["choice%s" %loopcount]=key
            continue  
    #Once it gathers every related account, it will ask you what you would like to delete.
    #Type the number value to delete it.
    if loopcount==0 or loopcount<0:
        printf("There were no results found.")
        printf("Press enter to return.")
        input()
        return
    printf("There were " + str(loopcount) + " results found.")
    for key,value in delete_selection.items():
        printf(key + ":" + value)
    printf("Type the corresponding number of the account you would like to delete: ",end='')
    up_for_deletion=input()
    #Once you type the number value, it finds the corresponding value and then pops it
    up_for_deletion="choice"+up_for_deletion
    printf("You would like to delete the account " + delete_selection[up_for_deletion] + "? (y/n)")
    while True:
        confirmation=input()
        if confirmation.lower()=='y' or confirmation.lower()=='yes':
            printf("Deleting " + delete_selection[up_for_deletion] + "...")
            saved_data.pop(delete_selection[up_for_deletion])
            #this gzip code will either compress or decompress the code, and then write the compressed code or read the decompressed code
            with gzip.open ('data.gz','w') as data:
                saved_data=pickle.dumps(saved_data)
                saved_data=gzip.compress(saved_data)
                data.write(bytes(saved_data))
            printf("Deletion finished.")
            break
        elif confirmation.lower=='n' or confirmation.lower=='no':
            printf("Action cancelled.")
            break
        else:
            printf("Incorrect input. Please respond with y or n:")
            continue
    return
    


       


#EDIT
#Edit will allow you to search for an account by site (like the delete function did) and will ask you what you want to change.
def edit():
    printf("Unfinished.")
    return




#SETTINGS           
#This is a program that lets you screw around with settings.
def settings():
    cls()
    while True:
        cls()
        printf("SETTINGS:\n*CLEAR ALL DATA\n*RUN DIAGNOSTICS\n*CHANGE PASSWORD*CLOSE")
        choice=input()
        if choice.lower()=='clear' or choice.lower()=='clear all data' or choice.lower()=='delete' or choice.lower()=='1':
            printf("Clearing data...")
            with gzip.open('data.gz','w') as data:
                brackets='{}'
                brackets=pickle.dumps(brackets)
                brackets=gzip.compress(brackets)
                data.write(bytes(brackets))
            printf("Done!")
            continue
        elif choice.lower()=='diagnostics' or choice.lower=='run diagnostics' or choice.lower()=='run':
            permission=adminpermission()
            if permission==True:
                diagnostics
            if permission==False:
                pass
        elif choice.lower()=='close':
            return
        else:
            printf("Please put in a valid input.")
            continue






#------------------------------------------------------
#lol this is the only code that actually gets executed, the rest is allllll functions, babyyyyyyy.
#savefile()
passwordverify()
while True:
    MainMenu()
