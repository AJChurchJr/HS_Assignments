

#Collaborated with Austin Heeter 
#Done by Andrew Church



import os
import time
import sys
ts=1
#code for auto-scrolling messages.
def printf(message, *word, end = "\n", sep = " "):
    for letter in message:
        print(letter, end = '', flush = True)
        time.sleep(ts*0.01)
    if word:
        for letter in word:
            print(letter, end = '', flush = True)
            time.sleep(0.01)
    else:
        pass
    if end == '':
        pass
    else:
        print("\n", end = '')
    return
with open("savednumbers.txt", "r") as saved_phone_numbers:
    phonebook=saved_phone_numbers.readline()
    phonebook=eval(phonebook)
#Clears the screen.
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

#This is the logo!
def logo():
    print("██████╗ ██╗ ██████╗ ██╗████████╗ █████╗ ██╗         ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗██████╗  ██████╗  ██████╗ ██╗  ██╗")
    time.sleep(0.1)
    print("██╔══██╗██║██╔════╝ ██║╚══██╔══╝██╔══██╗██║         ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝")
    time.sleep(0.1)
    print("██║  ██║██║██║  ███╗██║   ██║   ███████║██║         ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  ██████╔╝██║   ██║██║   ██║█████╔╝ ")
    time.sleep(0.1)
    print("██║  ██║██║██║   ██║██║   ██║   ██╔══██║██║         ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗ ")
    time.sleep(0.1)
    print("██████╔╝██║╚██████╔╝██║   ██║   ██║  ██║███████╗    ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗██████╔╝╚██████╔╝╚██████╔╝██║  ██╗")
    time.sleep(0.1)
    print("╚═════╝ ╚═╝ ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝")
    time.sleep(0.1)
    print("------------------------------------------------------------------------------")
    #This is the code for printing every phone number in your dictionary, accompanied by fancy letters!    
def print_all(phonebook):
    print(" _____        _____ _                  _____           _")
    time.sleep(0.1)
    print("|     |_ _   |  _  | |_ ___ ___ ___   |   | |_ _ _____| |_ ___ ___ ___ ")
    time.sleep(0.1)
    print("| | | | | |  |   __|   | . |   | -_|  | | | | | | | | | . | -_|  _|_ -|")
    time.sleep(0.1)
    print("|_|_|_|_  |  |__|  |_|_|___|_|_|___|  |_|___|___|_|_|_|___|___|_| |___|")
    time.sleep(0.1)
    print("      |___|                                                            \n")
    print("------------------------------------------------------------------------------")
    time.sleep(0.1)
    ts=1
    if len(phonebook)==0:
        printf("None.")
        print("------------------------------------------------------------------------------")
        printf("Press enter to continue", end='')
        input()
        return
    else:
        for key,value in phonebook.items():
            print("Name: " + str(key) + "       Number:" + str(value)+"\n")
            time.sleep(0.1)
        print("------------------------------------------------------------------------------")
        printf("Press enter to continue", end='')
        input()
        return

#This is the code for adding new phone contacts to your VIRTUAL PHONEBOOK!
def add(phonebook):
    #First, it will ask for the phone number. It does not take area codes or country codes.
    printf("Enter a phone number:", end='')
    temporary_phone_number=str(input())
    #These next two lines of code will check to see if it is a valid phone number by removing the dash and seeing if it has seven characters. Any more or any less and it will not register.
    phone_number_without_dash=list(temporary_phone_number)
    del phone_number_without_dash[3]
    phone_number_without_dash="".join(phone_number_without_dash)
    try:
        phone_number_without_dash=int(phone_number_without_dash)
    except:
        printf("Invalid phone number. Sending back to main menu.")
        return
    #If it is valid, it continues on like nothing happened.
    phone_number_without_dash=str(phone_number_without_dash)
    if len(phone_number_without_dash)==7:
        printf("Valid phone number.")
    #If it is invalid, it will delete the number and boot you back at the beginning.
    else:
        printf("Invalid phone number.")
        input("Press enter to restart.")
        return
    #Then, it will ask for the name the number belongs to.
    printf("Enter the name this person belongs to:", end='')
    temporary_name=input()
    #It gives you a preview and asks if you answered correctly.
    while True:
        printf("Your entry will be marked as: " + temporary_name + ":" + temporary_phone_number + "(y/n).", end='')
        choice=input()
        #If you answer yes, it registers.
        if choice.lower()=="y" or choice.lower()=="yes":
            printf("Action registered.")
            #ABC123
            phonebook[temporary_name]=temporary_phone_number
            with open("savednumbers.txt",'w') as saved_phone_numbers:
                saved_phone_numbers.write(str(phonebook))
            del choice
            return
        #If you enter no, it does not register.
        elif choice.lower()=="n" or choice.lower()=="no":
            printf("Action cancelled.")
            input()
            del choice
            return
        else:
            continue

#This is the code for removing a number from the phonebook. You can only do this with the name.
def remove(phonebook):
    if len(phonebook)==0:
        print("Your phone book is empty!")
        printf("Press enter to continue:", end='')
        input()
        return
    else:
        printf("Type the name of the person you would like to delete:", end = '')
        choice2=input()
        if choice2 in phonebook:
            printf("You would like to remove " + phonebook[choice2] + "?(y/n)", end='')
        else:
            printf("Invalid Name. Please check if you are using the correct capitalization. Press enter to return.", end='')
            input()
            return
        while True:
            choice=input()
            if choice.lower()=="y" or choice.lower()=="yes":
                phonebook.pop(choice2)
                print(choice2+" deleted.")
                printf("Press enter to continue", end='')
                input()
                del choice
                del choice2
                with open("savednumbers.txt",'w') as saved_phone_numbers:
                    saved_phone_numbers.write(str(phonebook))
                return phonebook
                #ABC123
            elif choice.lower()=="n" or choice.lower()=="no":
                print("Action cancelled.")
                printf("Press enter to continue", end='')
                input()
                del choice
                del choice2
                return phonebook
            else:
                printf("Answer with y or n:", end='')
                continue

#This is the code for searching for a phone number or name.
def search(phonebook):
    if len(phonebook)==0:
        print("Your phone book is empty!")
        printf("Press enter to continue", end='')
        input()
    else:
        while True:
            printf("Are you going to search by name(1) or by number(2), or do you want to exit to menu(3)?")
            choice=input()
            if choice.lower()=="1" or choice.lower()=="name":
                del choice
                printf("Enter the name of the person you are searching for:", end='')
                choice=input()
                if choice in phonebook:
                    printf(choice+"'s number is " + phonebook[choice])
                    continue
                else:
                    printf(choice + " is an invalid name.")
                    continue
            if choice.lower()=="2" or choice.lower()=="number":
                del choice
                printf("What number would you like to search up?",end='')
                choice=input()
                if choice in phonebook.values():
                    for key in phonebook:
                        if choice==phonebook[key]:
                            print(choice + " belongs to " + key)
                else:
                    printf("Number does not exist.")
            if choice.lower()=="3" or choice.lower()=="exit":
                del choice
                return

#This is the Booklet Menu, where all of the tasks can be executed!        
def bookletmenu(phonebook):
    printf('1. Print Phone Numbers')
    printf('2. Add a Phone Number')
    printf('3. Remove a Phone Number')
    printf('4. Lookup a Phone Number')
    printf('5. Clear sreen')
    printf('6. Quit')
    #The code below asks what task you would like to complete, and executes a specific function depending on what number you input.   
    choice=input("Type the number of the corresponing task you would like to complete:")
    if choice=="1":
        print_all(phonebook)
    if choice=="2":
        add(phonebook)
    if choice=="3":
        remove(phonebook)
    if choice=="4":
        search(phonebook)
    if choice=="5":
        cls()
    if choice=="6":
        with open("savednumbers.txt",'w') as saved_phone_numbers:
            saved_phone_numbers.write(str(phonebook))
        sys.exit(0)
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
logo()
time.sleep(0.1)
while True:
    bookletmenu(phonebook)