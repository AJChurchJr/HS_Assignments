"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
"""STRINGxVAL"""
string=input("Enter a word:") #input a
val=int(input("Enter a number:")) #input b
print(string*val) #multiplication
"""OUTPUTS
hello / 3 : hellohellohello
"""

"""5 CHARACTERS, ONE INPUT"""
lst=[] #declaration of value
for i in range(5):lst.append(input("Enter a word + ("+str(i+1)+"/5):")) #defining items to put into the list
for item in lst: print(item) #printing every item
"""OUTPUTS
hello everyone my name is: hello \n everyone \n my \n name \n is
howdy diddle dingly doo pals: howdy \n diddly \n dingly \n do \n pals
"""

"""CODE FIX
if 1 + 1 == 2
    print(2)
there is no colon after the if statement
"""

"""CODE FIX
while 1 == 1:
    print(5)
    Break
break should not be capitalized, also there is no need for a while statement that breaks the first line
"""


"""PRINTING THE NUMBER 5 VERY SMALL"""
for i in range(5):print(5) # prints 5 5 times
"""OUTPUTS
5
5
5
5
5
"""

