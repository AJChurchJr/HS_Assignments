"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
"""
The mode of a group of numbers is the value (or values) that occur most often (values have to occur more than once). Given a sorted list of numbers, return a list of all modes in ascending order.
Examples:
mode([4, 5, 6, 6, 6, 7, 7, 9, 10]) ➞ [6] 
mode([4, 5, 5, 6, 7, 8, 8, 9, 9]) ➞ [5, 8, 9]
mode([1, 2, 2, 3, 6, 6, 7, 9]) ➞ [2, 6] 
Notes
In this challenge, all group of numbers will have at least one mode.
"""

def mode(inputlist = None):
    #taking input if not present
    if inputlist is None:
        inputlist = input ("Enter a list of NUMBERS, separated by spaces.").split(" ")
    #input validation
    for i in range(len(inputlist)):
        try:inputlist[i]=int(inputlist[i])
        except:pass
    #counting every variable
    counter = {}
    for i in range(len(inputlist)):
        #adding value to the list if not present
        if inputlist[i] not in counter.keys():
            counter[inputlist[i]]=1
        #rising value if present
        else:
            counter[inputlist[i]]+=1
    #figuring out most used values
    mostUsed=[];highest=0
    for key,value in counter.items():
        if value == highest:
            mostUsed.append(key)
        elif value > highest:
            mostUsed.clear()
            highest=value
            mostUsed.append(key)
        else:
            continue
        
    #print(inputlist)
    #print(counter)
    #print(mostUsed)
    return mostUsed

print(mode())
#print(mode([4, 5, 6, 6, 6, 7, 7, 9, 10]))
#print(mode([4, 5, 5, 6, 7, 8, 8, 9, 9]))
#print(mode([1, 2, 2, 3, 6, 6, 7, 9]))

    

"""OUTPUTS:
mode([4, 5, 6, 6, 6, 7, 7, 9, 10]) ➞ [6] 
mode([4, 5, 5, 6, 7, 8, 8, 9, 9]) ➞ [5, 8, 9]
mode([1, 2, 2, 3, 6, 6, 7, 9]) ➞ [2, 6]
"""
