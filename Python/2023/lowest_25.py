"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
def lowest(list1 = None):
    #Values
    if list1 is None:
        list1 = input("Enter a list of numbers, divided by commas:").split(",") #input method
    total_subtracted = 0 #how much is taken from the list's larger characters
    #no input validation because it is unneeded
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    #checking for minimum
    minimum = min(list1)
    if list1.count(minimum) > 1:
        print("NO duplicate value.")
        return None
    #applying 25% debuff to larger items
    for i in range(len(list1)):
        if list1[i] != minimum:
            runner_up = list1[i] * 0.25
            list1[i] -= runner_up
            total_subtracted += runner_up
    #adding final value to smallest number
    for i in range(len(list1)):
        if list1[i] == minimum:
            list1[i] += total_subtracted
    return list1

"""OUTPUTS:
4,1,4 -> 3.0,3.0,3.0
6,10,8 -> 12.0, 7.5, 14.5
2,100 -> 27.0,75.0

"""
