"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
def string_math(s=""):
    total=0
    
    #inputs/values
    if s=="":s=input("MATH EQUATION: ")
    symbols,numbers=['+', '-', '(', ')',' '],['1','2','3','4','5','6','7','8','9','0']
    parenthesis,operators=['(',')'],['+','-']
    layers={}
    
    #validiity check
    for item in s:
        if item not in symbols and item not in numbers: print("INVALID");return
        
    #converting to list to help 
    tempList=[]
    for letter in s: tempList.append(letter)
    s=tempList;del tempList
    for i in range(len(s)):
        try:s[i]=int(s[i])
        except:continue
    print(s)
        
    #handling negatives -- this removes ALL OPERATORS because its JUST MERGING NUMBERS
    def negatives(s):
        while True:
            for i in range(len(s)):
                if i>0:
                    if type(s[i])==int and s[i-1]=="-":s[i]=s[i]*-1;del s[i-1];break
                    if type(s[i])==int and s[i-1]=="+":del s[i-1];break
            if i==len(s)-1:break
        return s
    s=negatives(s)
    print(s)
    
    #simplifying
    while True:
        for i in range(len(s)):
            if type(s[i]) == int and type(s[i+1]) == int:
                s[i+1]+=s[i]
                del s[i]
                break
        if i==len(s)-1: break
    print(s)
        
    #removing parenthesis
    while True:
        for i in range(len(s)):
            if s[i] in parenthesis:del s[i];break
        if i==len(s): break
    print(s)
        
    #RE-handling negatives 
    s=negatives(s)
    print(s)
    
    #solving
    while len(s)>0:
        total+=s[0]
        del s[0]
        continue
    #print(total)
    return total
    
print(string_math())

"""BUG REPORT
There is a bug in the program with parenthesis handling.
Instead of actually handling the layers and such within the parenthesis, it just simplifies everything inside said parenthesis and removes them
this would normally work, however if it has to handle negatives it spits out an incorrect number due to it not handling parenthesis within parenthesis
however, it works with the required inputs
"""
