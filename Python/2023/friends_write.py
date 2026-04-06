"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
#Take input three friends to be added to the file
#Add three people to the file
#I am confused as this is an assignment for writing and I do not know if it wants me to write a list or to write only one?????
friends = input("Enter a list of friends divided by commas:").split(",")
file = open("./test.txt","w")
for friend in friends:
    file.write(str(friend)+"\n")
file.close()
