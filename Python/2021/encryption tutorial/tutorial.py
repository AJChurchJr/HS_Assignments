import winsound
import pickle





input("DATA ENCRYPTION. PRESS ENTER TO ADVANCE EACH LINE.")
winsound.PlaySound("area1.wav", winsound.SND_ASYNC)
print('\n\n')
print('SECTION 1A, INTRODUCTION.')
input("*When you create a file for, as an example, handling usernames and passwords, you don't want people to just open the data files and see everything sitting out there, ESPECIALLY if nothing is being held server-side, and it's all client-side.")
input("*This is where encryption comes into place.")
input("*While it is a nice idea to create your own code so people can't just google how to crack it, sometimes you just want to prevent simple shenanigans from happening.")
input("*That is where importing things like pickle and gzip come along.")
print('\n\n')

print('SECTION 1B, VARIABLE CREATION.')
input("*First, let's create a regular variable. I made a string called 'variable.'")
variable=input("What would you like this variable to be?: ")
print("Here is our variable:", end='')
input(variable)
input("It is a " + str(type(variable)))
print('\n\n')

print('SECTION 1C, ENCRYPTING DATA.')
input("((First of all, import pickle.))")
input("*Now, let's create a *pickled* variable. A pickled variable is an object in which the variable or file is converted from a string, integer, float, list, dictionary, etc. into a BYTES-LIKE OBJECT.")
input("*You can convert the variable using pickle.dumps([variable]).")
picklevariable=pickle.dumps(variable)
print("Here is our pickled variable:", end='')
input(picklevariable)
input("It is a " + str(type(picklevariable)))
print('\n\n')

print('SECTION 1D, WRITING DATA TO A .PICKLE FILE.')
input("*If you check the code, right here I am writing this pickled variable to a .pickle file.")
input("*You use a normal 'with open()' statement and a .write statement.")
with open('data.pickle','w') as data:
    data.write(str(picklevariable))              
print('\n\n')

print("SECTION 1E, READING DATA FROM A .PICKLE FILE.")
input("*Now, let's read from a .pickle file.")
input("*We use with open() as usual, and use [filename].write.")
input("*Check the code if you want to see.")
with open('data.pickle','r') as data:
    input("*We use readline(), and then eval() to convert it into an encoded object, then pickle.loads() to unencrypt it!")
    readdata=data.readline()
    evaldata=eval(readdata)
    unpickled_data=pickle.loads(evaldata)
input("Our unpickled data is now what it was before:")
input(unpickled_data)
print('\n\n')









print("SECTION 2A, AN ISSUE WITH PICKLING.")
input("*Now, you may realize that, in your pickled statement, the string was just.. there, out in the open!")
print("*Look at this!")
input(picklevariable)
input("*You can just.. see exactly what you typed in that code. It's stupid!")
input("*Now, I honestly have no clue why it does this, but I know how to fix it.")
print('\n\n')

print("SECTION 2B, INTRODUCTION TO GZIP.")
input("*You have to import a new thing called 'gzip'.")
import gzip
input("*Apparently what GZIP does is compress the files further so you cannot read the text out in the open.")
input("*For example, let's use the variable you selected: " + variable)
input("*Then, we pickle it like before: " + str(picklevariable))
input("*And now, we use a new function called gzip.compress([variable])")
input("*You can ONLY do this if your variable is already encoded with pickle or another module.")
print("Gzipping the pickled code...")
zipvariable=gzip.compress(picklevariable)
print("Zipping finished!")
print("Your new variable should look like this:",end='')
input(str(zipvariable))
print('\n\n')

print("SECTION 3B, SAVING TO A .GZ FILE")
input("*Saving to a .gz file is somewhat different from saving to a .pickle and .txt file.")
input("*This time, you have to use 'gzip.open()' instead of just 'open()'")
input("*So, first, you need to have your pickled and gzipped variable, as an example, let's use yours.")
print("*Now, as an example, I'll execute the code:")
print("     with gzip.open('data.gz','w') as data:")
print("          data.write(bytes(zipvariable))")
input("and, just like that, your compressed and unreadable file has been saved to a proprietary file!")
print('\n\n')
#then it actually executes the code written in the print statement.
with gzip.open('data.gz','w') as data:
    data.write(bytes(zipvariable))

print("SECTION 3C, READING FROM A .GZ FILE")
input("*This one is quite self-explanatory. First, you need to gzip.open the file in read mode instead of write.")
input("*But then, you have to decode it, using modules that do the reverse of what we did before.")
with gzip.open('data.gz','r') as data:
    input("*First, use [read_data]=[filenickname].readline() in order to read what is on your file and put it on a variable.")
    read_data=data.readline()
    print("*It should look like your compressed variable, like this:")
    input(read_data)
    input("*Instead of using gzip.compress(), use gzip.decompress().")
    decompressed_data=gzip.decompress(read_data)
    print("*It should look like your old pickled variable, like this:")
    input(decompressed_data)
    input("*Then, use pickle.loads() in order to unpickle the variable.")
    unpickled_data=pickle.loads(decompressed_data)
    print("*It should look like your original variable, like this:")
    input(unpickled_data)
    print('\n\n')

print("SECTION 4, END.")
winsound.PlaySound("area2.wav", winsound.SND_ASYNC)
input("*That is the end of this small discovery I made.")
input("*It is quite helpful if you don't want people reading data files to see what does what.")
input("*Fair warning, however, it is *very* buggy. One example of which being the fact that .gz files corrupt if a stored dictionary gets edited too much.")
input("*But it works!")
input("fin")
    
