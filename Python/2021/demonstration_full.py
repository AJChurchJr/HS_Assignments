def cls():
    import os

    os.system('cls' if os.name=='nt' else 'clear')
    return
print("Created by Andrew Church.")
input("Hello world, the Python Demonstration.")

cls()
#basic print demo
print("Hello world!")
print("Hello " + "world!")
print("Hello","world!")
input("press enter to move on")

cls()
#variable demonstrations
variable="Hello world!"
print(variable)
del variable
input("press enter to move on")

cls()
#taking inputs
variable=input("Please type something here:")
print("Your item is " + variable)
input("press enter to move on")

cls()
#merging string variables
sliceone="Hello"
slicetwo="world!"
print(sliceone)
print(slicetwo)
print(sliceone+slicetwo)
del sliceone
del slicetwo
input("press enter to move on")


cls()
#every value type
stringvariable="Hello world!"
floatvariable=123.4
integervariable=123
booleanvariable=False
print(stringvariable)
print(floatvariable)
print(integervariable)
print(booleanvariable)
print(stringvariable , str(floatvariable) , str(integervariable), str(booleanvariable))
print(type(stringvariable))
print(type(floatvariable))
print(type(integervariable))
print(type(booleanvariable))
del stringvariable
del floatvariable
del integervariable
del booleanvariable
input("press enter to move on")


cls()
#math
print("1 + 1")
print(1 + 1)
print(2 * 2)
print(3 ** 3)
print(5 - 2)
print(6 / 3)
print(28//5)
variable=1+1
print(variable)
del variable
input("press enter to move on")

cls()
#if statements
variable=input("Type the letter b")
if variable == "b":
    print("Your input was correct!")
elif variable == "B":
    print("Your input was correct but it was a capital!")
else:
    print("Your input was NOT b!!!!!")
del variable
input("press enter to move on")

cls()
#loops
for i in range(5):
    print("Hello world!")

for i in range(5):
    if i == 1:
        variable='st'
    elif i == 2:
        variable='nd'
    elif i == 3:
        variable='rd'
    else:
        variable='th'
    print("This is the " + str(i) + str(variable) + " loop!")
    
length=6
for i in range(length):
    print(i)

del variable
del length
input("press enter to move on")



cls()
#functions
def FUNCTION(required_variable):
    print("Hello world!")
    print("The value given here is " + str(required_variable))
    return
FUNCTION("Hello World!")

def RETURNING_FUNCTION():
    return(2)
variable=RETURNING_FUNCTION()
print(int(variable) + 2)

del variable
input("press enter to move on")



cls()
#exec
variable = "print('Hello World!')"
exec(variable)
del variable
input("press enter to move on")


cls()
#classes and objects
class exampleclass:
    def __init__(self, num, string):
        self.num=num
        self.string=string
        print(num)
        print(self.num)
        print(string)
        print(self.string)
    def add_1_to_number(self):
        self.num=(int(self.num) + 1)
        print(self.num)
    def say_banana(self):
        self.banana=str( self.string + "banana" )
        print(self.banana)
        
variable=exampleclass(1,"pen")
variable.add_1_to_number()
variable.say_banana()
input("press enter to move on...")

cls()
#reading and writing
with open("examplefile.txt","r+") as examplefile:
    file=examplefile.read()
    print(file)
    file2=examplefile.readline()
    print(file2)
    examplefile.close()
with open("examplefile.txt","w") as examplefile:
    choice=input("What do you want to write to the file?")
    examplefile.write(str(choice))
    examplefile.close()
    print("Check the before hitting enter!")
input("press enter to continue...")
with open("examplefile.txt","w") as examplefile:
    examplefile.write("Hello world!")
    examplefile.close()
cls()

#However, none of these examples matter if you cannot do anything interesting with them.
        
