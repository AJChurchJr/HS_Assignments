import sys
import os
import time

#---------EASE OF ACCESS FUNCTIONS---------------
def printf(message, *word, end = "\n", sep = " "):
    for letter in message:
        print(letter, end = '', flush = True)
        time.sleep(0)
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

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return

def Reverse(lst): 
    return [ele for ele in reversed(lst)] 

#------CONVERSION FUNCITONS--------
def input_valid(argument):
    #It will run a try command where it tries to convert the input to an integer.
    #It does this so you can't give a word answer with letters.
    try:
        number_input=int(argument)
    except:
        print("Please put in a number.")
        validity=False
        return validity
    else:
        validity=True
        return validity

def check_if_list_is_binary(argument):
    for i in range(len(argument)):
        if argument[i]=='1' or argument[i]=='0':
            pass
        else:
            print("Your number is not binary!!!")
            validity=False
            return validity
    print("Number is binary.")
    validity=True
    return validity
        
def check_if_list_is_numbers(argument):
    #ARGUENT MUST BE A LIST OH MY GOD
    for i in range(len(argument)):
        pass

def input_to_str_list(argument):
    #This is self-explanatory
    try:
        number_input=str(number_input)
        number_list=list(number_input)
        return number_list
    except:
        print("Hey, developer, you made a mistake.")
        return argument

    
    
def input_to_int_list(argument):
        #Once you put in a number, it will convert it into a string, and then a list.
        number_input=str(argument)
        number_list=list(number_input)
        #Once the variable is in a list, it will convert everything in the list into an integer
        #This was quite confusing at first, so Mr. Walker gave me an example on how he would do it.
        #First, you create a second list.
        number_list2=[]
        #Then, you do a for loop where it appends an integer version of each of the first list's value to the second list
        for i in range(len(number_list)):
            number_list2.append(int((number_list[i])))
        #Then, it returns!
        return number_list2



def list_to_str(argument):
    #First, it takes your list, and, in a for loop, converts it into a string.
    try:
        binstring=''
        argument=binstring.join(argument)
        return argument
    #Oh, and it yells at you if I make a mistake.
    except:
        print("Hey, developer, you made a mistake.")
        return argument
    
    
    
    


#----------BINARY FUNCTIONS------------
def d2b():
    cls()
    printf("DECIMAL TO BINARY CONVERSION")
    printf("Please enter the number you would like to convert:",end='')
    #The program asks for the number you would like to convert.
    number_input=input()
    printf("Testing..")
    #It then runs the validity test.
    validity=input_valid(number_input)
    if validity==False:
        return
    elif validity==True:
        pass
    printf("First, we must configure your number input to turn it into an integer.")
    printf("Configuring...")
    #It checks to see if your argument is a string or a list, and then converts it into an integer because this function only requires integers.
    if type(number_input)==list:
        num=list_to_str(number_input)
        num=int(num)
    elif type(number_input)==str:
        #I don't need to try this because I already did a checker function that would have caught any errors.
        num=int(number_input)
    print(num)
    print("We are now converting your number...")
    binary_number=[]
    while True:
        #This will run a division algorithm to check what values are 1s and what values are 0s
        #It will repeatedly divide the numbers by 2, adding the remainders of 1 or 0 to a list.
        #It repeatedly checks if the divided number is greater than 0. When it is no longer greater than 0, it will end the loop.
        divided_number=num//2
        remainder=num%2
        num=divided_number
        binary_number.append(str(remainder))
        if divided_number>0:
            continue
        else:
            break
    #Once the loop is finished, it will reverse the loop to get the binary number.
    binary_number=Reverse(binary_number)
    binary_str=''
    binary_number=binary_str.join(binary_number)
    print("Conversion finished!")
    printf("Your binary number is " + str(binary_number))
    input("Press enter to exit.")
    
        
        





def b2d():
    cls()
    printf("BINARY TO DECIMAL CONVERSION")
    printf("Please enter the number you would like to convert:",end='')
    #The program asks for the number you would like to convert.
    number_input=input()
    printf("Testing..")
    #It then runs the validity test.
    validity=input_valid(number_input)
    if validity==False:
        return
    elif validity==True:
        pass
    
    
    #First, this program converts your string input into a list.
    numberlist=input_to_int_list(number_input)
    validity=check_if_list_is_binary(number_input)
    if validity==False:
        return
    if validity==True:
        pass
    printf("We are now converting your number...")
    #It reverses the list so it can algorithmically find out what number's value is what.
    backwards_list=Reverse(numberlist)
    #Then, it will begin counting.
    counter=1
    total=0
    #If I equals 1, it adds the corresponding value to the total. Once the loop is finished, it will print the total.
    for i in range(len(backwards_list)):
        if backwards_list[i]==1:
            total+=counter
        elif backwards_list[i]==0:
            pass
        else:
            print("error.")
            return
        counter*=2        
    printf("Your number is " + str(total))
    input("Press enter to continue...")
    return

#------------------ASKII FUNCTIONS------------------
def chartoask():
    printf("Please enter the text you would like to convert:",end='')
    #First, it converts your number into a string, and then a list.
    num=input()
    num=str(num)
    num=list(num)
    print(num)
    converted_num=[]
    #Then it runs a for loop, converting each ascii asset in it with its corresponding number
    for i in range(len(num)):
        converted_num.append(ord(num[i]))
    printf("Your askii text is:")
    for i in range(len(converted_num)):
        #And then it prints it all.
        print(str(converted_num[i]) + " ", end='')
    print('\n')
    input("Press enter to exit.")

def asktochar():
    printf("Enter the list of numbers you would like to convert, with each number separated by a space and nothing more:")
    num=input()
    dictnum=num.split(" ")
    printf("Converting...")
    #This runs a for loop in a try and except, where it will yell at you if you input something incorrectly.
    try:
        for i in range(len(dictnum)):
            dictnum[i]=chr(int(dictnum[i]))
    except:
        print("ERROR. YOU DID NOT PUT IN ASCII. NO LETTERS.")
        return
    converted_str=''
    #Then it appends every letter to an empty string and prints it.
    for i in range(len(dictnum)):
        converted_str=converted_str+str(dictnum[i])
    print(converted_str)
    
        
        


    
def mainmenu():
    cls()
    printf("Hello! Welcome to your BINARY-DECIMAL CONVERSION TOOL.")
    #This basically asks what you want to do
    while True:
        printf("BINARY CONVERSION(1) OR ASKII CONVERSION(2)")
        choice=input()
        if choice.lower()=='1':
            printf("CONVERT DEC TO BINARY (1) OR CONVERT BINARY TO DEC(2)")
            choice=input()
            if choice.lower()=='1':
                   d2b()
            elif choice.lower()=='2':
                   b2d()
            break
        elif choice.lower()=='2':
            printf("ASKII TO CHARACTERS (1) OR CHARACTERS TO ASKII(2)")
            choice=input()
            if choice.lower()=='1':
                asktochar()
            if choice.lower()=='2':
                chartoask()
        else:
            printf("Put in a valid input.")
            continue
    return
    
    


while True:
    mainmenu()
