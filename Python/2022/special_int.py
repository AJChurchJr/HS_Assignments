"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
"""PSEUDOCODE
-declaration
    -take an input for a number
    -make a list for special integers
-do a for loop for the range of the input, i+1 because of how it does iterations
    -split the number into a list of its individual digits
    -check for duplicate values
    -if there are no duplicate values, append to the list
-output prints
    -print the number of special integers
    -print every special integer included
"""
#taking input
n=int(input("Enter a number:"))
special_integers=[]
nonspecial_integers=[]
#the loop
for i in range(n):
    #this is the current number, put into a string for easier converting
    cur_num=str(i+1)
    #this is a sort of switch. by the end of cur_num, if the switch is still True, it appends to special_numbers
    special=True
    #iterates through the string number
    for item in cur_num:
        #checking for duplicate values
        if cur_num.count(item) > 1:
            nonspecial_integers.append(cur_num)
            special=False
            break
    #if there were NO duplicate values, it then appends the value to special_integers
    if special: special_integers.append(cur_num)
print("============SPECIAL============")
print(len(special_integers))
print('--')
for item in special_integers: print(str(item)+"/",end="")
print('--')
print("==========NONSPECIAL===========")
print(len(nonspecial_integers))
print('--')
for item in nonspecial_integers: print(str(item)+"/",end="")
print('--')    
"""OUTPUTS
12: 11 special, 1 nonspecial
123: 100 special, 23 nonspecial
135: 110 special, 25 nonspecial
999: 738 special, 261 nonspecial
"""

