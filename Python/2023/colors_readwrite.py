"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
colors = []
for i in range(3):
    colors.append(input("ENTER A COLOR: "))
#input
with open("./test.txt","r+") as file:
    for color in colors:
        file.write(str(color)+"\n")
#output
with open("./test.txt","r") as file:
    print(file.read())
    
