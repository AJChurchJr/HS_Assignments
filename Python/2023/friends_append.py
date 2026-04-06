"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
#CREATING A LIST
def create_list():
    #startup info
    print("CREATING LIST==========")
    print("Filename: test.txt")
    file = open("test.txt","w")
    
    #inputting friends
    friends = input("Enter friends, separated by commas\n>").split(",")
    
    #writing friends to file
    for friend in friends:
        file.write(str(friend)+"\n")
    file.close()
    
    #finishing info
    del friend, friends, file
    print("Done!")

    
#ADDING TO A LIST  
def add_list(arg=None):
    #startup info
    print("ADDING TO LIST==========")
    file = open("test.txt","a")
    
    #taking input if none is provided
    if arg is None:
        arg = input("Enter friend\n>")
    file.write(str(arg)+"\n")
    
    #finishing info
    file.close()
    del file,arg
    print("Done!")

    
#DISPLAYING LIST
def display_list():
    #startup info
    print("DISPLAYING LIST==========")
    file = open("./test.txt","r")
    #output
    print(file.read())
    #finishing info
    file.close()
    del file
    print("Done!")



#startup info
print("==========WELCOME==========")
index = "a"
while index in "abc":
    #taking input
    index = input(
    "a) Create new list\nb) Add name to the list\nc) Display the list\nd) Quit\n>"
    ).lower()

    print("==========",end="")
    if index == "a":
        create_list()
    elif index == "b":
        add_list()
    elif index == "c":
        display_list()
    else:
        print("EXITING")



    
