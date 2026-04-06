"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
"""FRACTION MATH PSEUDOCODE
-take an input
-split the number by their top and bottom numbers, splitting them into a 2-index list
-multiply both the numerator and denominator of num A by the denominator of num B
-multiply both the numerator and denominator of num B by the denominator of num A

-request input for the two items, add, subtract, multiply, divide
-for add/subtract: add/subtract the numerators
-for multiply/divide: 

"""
def div():print("====================")
#input
numA=input("Enter a fraction, divided by a /:").split("/")
numB=input("Enter another fraction:").split("/")
div()
#turning items into integers
for i in range(2):
    numA[i]=int(numA[i])
    numB[i]=int(numB[i]) #it also modifies numB since they will be the same length
#LCM simplifying
original_denominators=[numA[1],numB[1]]
numA[0]*=original_denominators[1]
numA[1]*=original_denominators[1]
numB[0]*=original_denominators[0]
numB[1]*=original_denominators[0]
del original_denominators #RAM saving
#displaying fractions
print("SIMPLIFIED:")
print(str(numA),str(numB))
div()
#taking input for operations
available_choices=["0","1","2","3"];choice=5 #temporary values for the menu
while choice not in available_choices:
    choice=input("Would you like to:\nadd(0)\nsubtract(1)\nmultiply(2)\ndivide(3)\n")
if choice=="0":
    output=[(numA[0]+numB[0]),numA[1]]
if choice=="1":
    output=[(numA[0]-numB[0]),numA[1]] 
if choice=="2":
    output=[(numA[0]*numB[0]),(numA[1]*numB[1])]
if choice=="3":
    output=[(numA[0]*numB[1]),(numA[1]*numB[0])]
#OUTPUTS, INCLUDING FIXING THINGS
div()
if output[0]==output[1]:output=1
elif output[0]==0:output=0
if type(output)==list:
    print("OUTPUT:\n"+str(output[0])+"/"+str(output[1]))
else:
    print("OUTPUT:\n"+str(output))
"""OUTPUTS
1/2 1/2 divide: 1
1/2 2/4 divide: 1
1/5 1/5 subtract: 0
1/5 1/5 add: 10/25
1/5 1/5 multiply: 25/625
"""
