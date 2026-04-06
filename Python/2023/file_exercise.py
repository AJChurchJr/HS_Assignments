"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
"""NOTES FOR THE KROOG:
line count is done in line_by_line
removing newline is done by word_count
highest word frequency and length is done by word_count
"""

def div():
    print("="*30)

def restore():
    if input("Enter anything to reset file. Leave blank to leave.") != "":
        with open("test.txt","w") as file:
            file.write("""What is Python language?                                                
Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in 
languages such as C++ or Java. 
Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.The best way we learn anything is by practice and exercise questions. We  have started this section for those (beginner to intermediate) who are familiar with Python.""")


            
def full_read():
    #read file
    with open("test.txt","r") as file:
        file = file.read()
    print("OUTPUT:",str(file))


#read first n lines
def read_start():
    n=int(input("How many lines to read (start)?:"))
    with open("test.txt","r") as file:
        file = file.read()[:n]
    print("OUTPUT:",str(file))

#read last n lines
def read_end():
    n=int(input("How many lines to read (end)?:"))
    with open("test.txt","r") as file:
        file = file.read()
        file = file[ (len(file)-1 -n):] 
    print("OUTPUT:",str(file))


#read file line by line in list
def line_by_line():
    with open("test.txt","r") as file:
        file = file.read().split("\n")
    print("OUTPUT:",str(file),"| line count",str(len(file)))

#counting each word
def word_count():
    count = {}
    highest = [("",0)]
    longest = [("",0)]
    with open("test.txt","r") as file:
        file = file.read().split(" ")
        for word in file:
            word = str(word).lower()
            #error checking: empty words
            if word == "" or word == " ": continue
            #error checking: \n
            if "\n" in word:
                word = word.replace("\n","")
            #actual word count
            if str(word).lower() not in count.keys():
                count[word]=1
            else:
                count[word]+=1
            #updating highest word frequency
            if count[word] > highest[0][1]:
                highest = [(word,count[word])]
            elif count[word] == highest[0][1]:
                highest.append((word,count[word]))
            #updatng longest word
            if len(word) > longest[0][1]:
                longest = [(word,len(word))]
            elif len(word) == longest[0][1]:
                longest.append((word,len(word)))
    print("HIGHEST FREQUENCIES ARE",str(highest))
    print("LONGEST WORDS ARE",str(longest))
          

#copying file
def copy_file():
    #making new file
    copy = str(input("What file are you copying to?\n>"))
    if "." not in copy: copy += ".txt"
    copy = open(copy,"w")

    #reading original file
    orig = open("./test.txt","r")
    orig_read = orig.read()
    orig.close()

    #writing
    copy.write(str(orig_read))
    copy.close()

    print("COMPLETE.")

#writing a list to the file
def write_list(user_input:list = None):
    if user_input == None:
        user_input = input("Please enter a list of items, separated by commas\n>").split(",")
    with open("./test.txt","w") as file:
        file.write(user_input)
    print("COMPLETE | you can use eval(file.read()) to make it readable!")
    
    
    
    
            

functions = {
    "a":"full read",
    "b":"read starting lines",
    "c":"read ending lines",
    "d":"split lines into list",
    "e":"word count",
    "f":"copy file",
    "x":"exit"}

def main():
    restore()
    
    #telling to run ; this is so it can stop the loop at any time without manually quitting
    run = True

    while run:
        div()
        
        choice = ""
        #displaying arguments
        for k,v in functions.items():
            print("|",str(k),":",str(v))
        #taking input
        while choice not in functions.keys():
            choice=input(">").lower()

        #running functions based on arguments
        if choice == "x":
            run = False
        elif choice == "a":
            full_read()
        elif choice == "b":
            read_start()
        elif choice == "c":
            read_end()
        elif choice == "d":
            line_by_line()
        elif choice == "e":
            word_count()
        elif choice == "f":
            copy_file()
            

main()

exit()
