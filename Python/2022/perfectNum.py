

"""
-----CHECK FOR-----
Positive integer
Equal to:
    sum of ALL of its positive divisors
    plus the number itself
    divided by two


-----PSEUDOCODE-----
Take a number -- stored as a variable
Create for-loop with number
Checks with every number (i, in this case) to see if the selected number can divide by it to leave a whole number
If not, it moves on to the next number
If so, it adds it to a list
The for-loop ends when the number doing the dividing is greater than the selected number
Once this finishes, it checks a statement that looks like this:
    selectedNum = (selectedNum + sumList) /2
If the statement is true, the code returns "True"
If not, it returns "False"
"""


def perfectNum(selectedNum):
    #Checking for user error
    try: selectedNum = int(selectedNum)
    except: print("Your number is imperfect"); return False 

    #Checking to see if a number is a divisor or not
    divisorList = []    
    for i in range(selectedNum):
        
        index = i+1; currentDivide = selectedNum / index
        
        if float(currentDivide) == int(currentDivide): divisorList.append(int(currentDivide))
        
        else: continue

    #Doing the calculations
    totalSum = 0
    for item in divisorList: totalSum += item
    totalSum /= 2
    if totalSum == selectedNum:
        print("Your number is perfect.")
        return True
    else:
        print("Your number is imperfect.")
        return False



#Taking input
while True:
    selectedNum = input("Please enter a number: ")
    perfectNum(selectedNum)
    print("\n")

