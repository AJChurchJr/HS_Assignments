"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
import random
#convert list from least to greatest
#take parameters search and list (LIST CAN BE PRE-DEFINED)
def binSearch(lst=[1,2,3,4,5],search=2):
    #my problem with this assignment is that the article literally says how to program it.
    #they are programming it the exact same way I was planning to program it
    #it looks like plagiarism 
    low,high=0,(len(lst)-1)
    while (low <= high):
        middle=(low+(high-low)//2)
        if lst[middle]==search:return (True,middle)
        elif lst[middle]<search:low=middle+1
        else:high=middle-1
    return (False,0)
    
def iv(text):# makes an input statement and converts it to int with try-except
    while True:
        try:val=int(input(text));return val
        except: continue     
    
#LIST must be added in CODE to prevent UNNECESSARY UNREADABILITY
lst=[1]
for i in range(random.randint(5,(iv("Enter MAX length of list:")-1))):lst.append(lst[i]+random.randint(0,5))
print("Your list is: ",str(lst)) 
search=iv("Enter a SEARCH: ")
result=binSearch(lst,search)
if result[0]: print("Item",str(search),"FOUND at index",str(result[1]))
else: print("Item",str(search),"NOT FOUND")
