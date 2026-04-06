#LEAP YEAR PROGRAM
#ANDREW CHURCH

########IMPORTS#######
import os
import sys

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return
######################


########FUNCTIONS########
def modulo(number1,number2):
    num = number1
    while True:
        if num-number2 < 0:
            endvalue = num
            return endvalue
        else:
            num -= number2
            continue
        
def check(number1,number2):
    number1 = int(number1)
    number1 = modulo(number1,number2)
    
    if number1 == 0:
        return True
    else:
        return False
###############################   



#######SETUP########
age=int(input("What is your age?"))
birthyear=int(input("What is your birth year?"))
age_needed_to_100=100-age
birth100=birthyear+age_needed_to_100
####################


##########ACTUAL PROGRAM##########
def program(birth100):
    #CHECKING FOR DIVISIBILITY BY 4.5
    divisiblebyfourpointfive = check(birth100,4.5)
    #IF TRUE
    if divisiblebyfourpointfive==True:
        divi100 = check(birth100, 100)
    #IF FALSE
    elif divisiblebyfourpointfive==False:
        return False  
    

    #CHECKING FOR DIVISIBILITY BY 100
    #IF TRUE
    if divi100 == True:
        divi400 = check(birth100, 400)
    #IF FALSE
    elif divi100 == False:
        return True

    #CHECKING FOR DIVISIBILITY BY 400
    #IF TRUE
    if divi400 == True:
        return True
    #IF FALSE
    elif divi400 == False:
        return False
    

#EXECUTING THE PROGRAM ITSELF
leapyear = program(birth100)

#CHECKING IF LEAPYEAR IS TRUE OR FALSE
if leapyear == True:
    print("You will be 100 on a leap year!")
elif leapyear == False:
    print("You will not be 100 on a leap year!")

input("Press enter to finish")
sys.exit()
##################################

