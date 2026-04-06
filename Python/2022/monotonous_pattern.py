"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""

#default values
numbers=input("Enter a list of numbers, separated by commas :").split(",")
failsafe=False
pattern_to_follow=None

#converting to integers
for i in range(len(numbers)):
    try:numbers[i]=int(numbers[i])
    except:print("Not a monotonous pattern.");exit()
    
#testing the numbers for output
for i in range(len(numbers)-1):
    #checking if the values are increasing
    if i==0 and numbers[i] < numbers[i+1]:
        pattern_to_follow="increasing"
    #checking if the values are decreasing
    elif i==0 and numbers[i] > numbers[i+1]:
        pattern_to_follow="decreasing"
    #if neither are true, the failsafe is tripped because there is a duplicate number
    else: failsafe=True
    #if a pattern is already discovered, it will test and see if this applies everywhere
        #specifically, it will check if the opposite has occurred in order to trip a failsafe
    if pattern_to_follow=="increasing" and numbers[i] >= numbers[i+1] : failsafe=True
    if pattern_to_follow=="decreasing" and numbers[i] <= numbers[i+1] : failsafe=True

#output
if not failsafe: input(pattern_to_follow)
else: input("pattern not monotonous")


"""OUTPUTS
1,2,3,4,5 : increasing
5,4,3,2,1 : decreasing
5,2,-1,-5 : decreasing
5,4,3,4,5 : pattern not monotonous
a,b,c,d,e,f : pattern not monotonous
1,2,3,a,5,6 : pattern not monotonous
None : pattern not monotonous
19,19,5,5,5,5,5 : pattern not monotonous
"""
