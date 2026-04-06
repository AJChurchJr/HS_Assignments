#Created by Andrew Church
#3/18/2021
#SHUFFLE FUNCTION FROM ADAM WALKER
#SLIGHT HELP RECEIVED FROM KYLE

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return

import sys
import os
import time
import random

def shifter():
    while True:
        shift=input("How far would you like your shift to be?:")
        #First, it checks to see if your shift is a number or not
        try:
            shift=int(shift)
        except:
            input("Please put in a number.")
            continue
        if shift<0:
            input("Please put in a number.")
            continue
        if shift>25:
            input("Shift too large. Please pick a shift 25 characters or shorter.")
            continue
        else:
            break
    return shift
    

#This asks for the number you want to encode
#It then asks how would you like to encode it
def mainmenu():
    output=''
    your_text=input("Please enter the text you would like to encode:")
    print(your_text)
    while True:
        cls()
        print("Input: " + your_text)
        choice=input("How would you like to encode your number?\n1.Caesar\n2.Reverse\n3.Atbash\n4.randomscramble\n5.surprise!\n6.New Input\n7.Set Output As Input\nOutput: " + output + '\n')
        if choice.lower()=='1':
            output=caesar(your_text)
        elif choice.lower()=='2':
            output=reverse(your_text)
        elif choice.lower()=='3':
            output=atbash(your_text)
        elif choice.lower()=='4':
            output=shuffle(your_text)
        elif choice.lower()=='5':
            output=surprise(your_text)
        elif choice.lower()=='6':
            your_text=input("Please enter your new text:")
            continue
        elif choice.lower()=='7':
            your_text=output
            output=''
            continue
        else:
            print("Put in a valid input.")
            continue


#------------THE ENCODING METHODS-----------------
def atbash(your_text):
    #This creates 5 different lists, ones for numbers, atbash, alphabet, and their corresponding uppercase values.
    #Though, I have removed a lot of those lists because I found simpler methods of doing this.
    #It will find the index of one number and plug that index into another number.
    nums=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    atbash=['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
    numbervalues=[]
    output=[]
    #Though, this is slightly complicated due to the fact that I want to have uppercases remain uppercase in the conversion method
    for i in range(len(your_text)):
        try:
            if your_text[i].isupper()==True:
                    #It creates an item that is going in next, and does the required conversions needed to put it in as an output
                    queue=''
                    #First it copies the value
                    queue=your_text[i]
                    #Oh, it also has to convert it into a lowercase temporarily
                    queue=queue.lower()
                    #Then it finds the index of that number in the alphabet list
                    queue=alpha.index(queue)
                    #Then it puts that index into the atbash to find the corresponing value
                    queue=atbash[queue].upper()
                    output.append(queue)
            elif your_text[i].isupper()==False:
                    #This does the EXACT SAME THING as the uppercase one, but does not convert the letter back into uppercase once it goes lower
                    queue=''
                    queue=your_text[i]
                    queue=queue.lower()
                    queue=alpha.index(queue)
                    queue=atbash[queue]
                    output.append(queue)
        except:
            output.append(queue)

    output=''.join(output)
    return output
            
            
            

def reverse(your_text):
    #What this will do is take your text and reverse it, however you have to define reverse since there is no handy function that does it for you
    #First, the program creates an empty dictionary
    your_dict={}
    #Then, it runs a for loop, giving each letter a number key
    for i in range(len(your_text)):
        your_dict[i]=your_text[i]
    #Then, it runs another for loop where it appends the highest value in the dictionary into a list, then pops it from the dictionary
    your_list=[]
    for i in range(len(your_dict)):
        #It finds the max key here
        up_for_adding=max(your_dict.keys())
        your_list.append(your_dict[up_for_adding])
        your_dict.pop(up_for_adding)
    output=''.join(your_list)
    return output
    
        
        


#This asks how far you want to shift your text, and then shifts it with the cursed code
def caesar(your_text):
    shift=shifter()
    #Then, it converts your input to a list, and then creates an empty list for your ascii text and your fully converted text.
    your_text=list(your_text)
    your_ascii_text=[]
    your_new_text=[]
    #Then, it runs a for loop converting each character to an ascii character, shifting it by your shift input.
    for i in range(len(your_text)):
        #It will run a check to see if your ascii number is in the uppercase or lowercase section.
        if ord(your_text[i])>64 and ord(your_text[i])<91:
            #If it is in the uppercase section, it will check and see if your shift is higher than the range of uppercase section of letters, and then it will move it back to the beginning and continue going up.
            #print(your_text[i])
            #print(ord(your_text[i]))
            #print(shift)
            if (ord(your_text[i]) + shift)>90:
                overflowingtext=ord(your_text[i])+shift
                your_ascii_text.append(64+(overflowingtext)-90)
            else:
                your_ascii_text.append(ord(your_text[i]) + shift)

        elif ord(your_text[i])>96 and ord(your_text[i])<123:
            #If it is in the lowercase section, it does the same as last time, but changes the ASCII characters to fit a lowercase variant
            if (ord(your_text[i]) + shift)>122:
                overflowingtext=ord(your_text[i])+shift
                your_ascii_text.append(96+(overflowingtext)-122)
            else:
                your_ascii_text.append(ord(your_text[i]) + shift)
        else:
            your_ascii_text.append(ord(your_text[i]))
            
    #Then, it converts your shifted ascii back to a string
    for i in range(len(your_ascii_text)):
        your_new_text.append(chr(your_ascii_text[i]))
    #It glues it back together, then prints it.
    your_new_text=''.join(your_new_text)
    return your_new_text

#This is a horrible, discombobulated mess on purpose. There are no comments explaining anything on purpose.  
def surprise(argument):
    #conversion to list
    argument=list(argument)
    for i in range(len(argument)):
        argument[i]=argument[i].lower()
    argument=''.join(argument)
    argument=list(argument)
    #banan
    for i in range(len(argument)):
        argument[i]='banan'+argument[i]
    argument=''.join(argument)
    argument=list(argument)
    #pple
    for i in range(len(argument)):
        if argument[i].lower()=='a':
            argument[i]=argument[i]+"pple"
    argument=''.join(argument)
    argument=list(argument)
    #ear
    for i in range(len(argument)):
        if argument[i].lower()=='p':
            argument[i]=argument[i]+'ear'
    argument=''.join(argument)
    argument=list(argument)
    #angerine
    for i in range(len(argument)):
        if argument[i].lower()=='r':
            argument[i]=argument[i]+'aspberry'
    argument=''.join(argument)
    argument=list(argument)
    for i in range(len(argument)):
        if argument[i].lower()=='g':
            argument[i]=argument[i]+'rapes'
    argument='thiscipherisfruity'.join(argument)
    print(argument)
    return argument
    




    
#OBTAINED FROM MR WALKER      
def shuffle(argument):
    import random

    string_temp = list(argument)
    random.shuffle(string_temp)
    string_final = ''.join(string_temp)

    return string_final            
        
    
    
    
    






while True:
    mainmenu()
