"""
take three rolled numbers as an argument
run arguments through a function to see if x+y or x*y is equal to z
if correct, say WIN
if incorrect, say LOSE
"""

import sys
while True:
    #startup text
    print("======CHUCKWALLA======")
    print("-ENTER 'DONE' TO EXIT-")
    #taking input - dividing input into individual indexes
    choices=input("Please enter 3 numbers divided by spaces: ").split(" ");lst=[]
    for item in choices:
        try:
            lst.append(int(item))
        except:
            if item.lower()=="done": sys.exit()
    if len(lst)>3 or len(lst)<3:print("ERR 1: LIST INSUFFICIENT");sys.exit()        
    #debug prints
    #print(lst);print(lst[0]+lst[1]);print(lst[0]*lst[1])
    #individual indexes used to check for a chuckwalla
    n=[(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)] #n are all the indexes
    for i in range(len(n)):
        if (lst[n[i][0]]+lst[n[i][1]]==lst[n[i][2]]) or (lst[n[i][0]]*lst[n[i][1]]==lst[n[i][2]]):
            print("Chuckwalla: YOU WIN");chuckwalla=True
            break

        else: chuckwalla=False; continue

    if not chuckwalla: print("No Chuckwalla: YOU LOSE")
