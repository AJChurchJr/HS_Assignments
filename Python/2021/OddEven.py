import time

#Checks if a number is even or odd
def check_even_odd(num):
    if num % 2 == 1:
        evenodd="odd"
    elif num % 2 == 0:
        evenodd="even"
    else:
        return "error"
    return evenodd

#Modifies the number depending on if the number is even or odd
def modify(num,evenodd):
    if evenodd=='odd':
        num*=3
        num+=1
        return num
    elif evenodd=='even':
        num/=2
        return num


def make_list_to_1(num):
    #Makes a list
    lisst=[]
    #Checks if the number is equal to 1, or even, or odd.
    #Then, in response, will modify the number accordingly.
    #If the number is equal to 1 the code quits
    while True:
        numtype = check_even_odd(num)
        lisst.append(num)
        if num == 1:
            return lisst
        if numtype == 'odd':
            num=modify(num,'odd')
            continue
        elif numtype == 'even':
            num = int(modify(num, 'even'))
            continue

#Loops the program indefinitely.
def loop(num):
    loopcount = 1
    while True:
        list=make_list_to_1(num)
        print(list)
        print("Highest number was ", str(find_greatest(list)))
        print("Done with iteration", loopcount)
        print("",end='\n')
        loopcount+=1
        num+=1
        time.sleep(1)

def find_greatest(list):
    highest=0
    for item in list:
        if item>highest:
            highest=item
    return highest


#Takes input
def take_input():
    while True:
        try:
            num = int(input("Insert a number:"))
            if num < 1:
                print("no negatives")

        except:
            print("Invalid number")
            continue

        break

    return num



num=take_input()
loop(num)