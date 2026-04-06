
# THIS IS A PROGRAM THAT SCANS YOUR ENTIRE HARD DRIVE
# IT THEN STORES A "QUERY" FILE THAT IS JUST A PLAINTEXT CSV LIST
# AND THEN IT OPENS THE FILE, GENERALLY WITH ANOTHER APPLICATION
# IT USES RECURSION FOR SUBFOLDERS
import os, sys, time, random, subprocess, platform

#self explanatory
verbose = False
def printv(*args):
    if verbose:
        for arg in args:
            print(arg, end = " ")
        print()


# indexes every file in a directory including subdirectories
def perform_search(path:str="./",subfolders:bool=False,extensions:tuple=None) -> list:
    output=[]
    printv("---\nPERFORMING SEARCH IN", path, "WITH" if subfolders else "WITHOUT", "SUBFOLDERS WITH", extensions, "EXTENSIONS")
    # error checking
    if not os.path.isdir(path): 
        printv("ERROR: PATH IS NOT A DIRECTORY")
        return output
    # this generates a list indexing every single file
    for i in os.listdir(path):
        file_full = os.path.join(path,i)
        if os.path.isfile(file_full):
            # checking for file extension requirements
            if i[0] == "." and i[1] == "_":
                printv("._ ERROR FILE SKIPPED", file_full)
            elif len(extensions)<=0 or  os.path.splitext(i)[1].lower() in extensions:
                output.append(file_full)
                printv("ADDED",file_full)
            else:
                printv("WRONG EXTENSION FROM",file_full)
        # if the path file is a directory, it uses recursion to fetch that subdirectory too
        if os.path.isdir(file_full):
            if subfolders:
                #adds subfolder outputs to current
                output += perform_search(path=file_full,subfolders=True,extensions=extensions)
            printv("FOUND SUBFOLDER", file_full)
    # returning output when done
    printv("SUCCESSFUL SEARCH WITH ", len(output), "RESULTS")
    return output


# saving indexed list to a file
def save_to_file(output:list,path:str="./output.csv"):
    printv("---\nSAVING FILE TO",path)
    # making sure the output is a proper list
    if type(output) not in (list,tuple,set):
        printv("INPUT WAS NOT A LIST")
        return 
    #converting output to a string
    printv("CONVERTING OUTPUT TO STRING")
    str_output = ""
    for file in output:
        str_output+=(file+",")
    printv("SAVING FILE")
    # making sure no weird file shennanigans happens, and saving if it nothing does
    try:
        with open(path,"w") as file:
            file.write(str_output)
        printv("SUCCESSFUL SAVE TO", path)
    except Exception as e:
        printv("ERROR: INVALID FILE (idk how you do that with this lol)")


# loading indexed list from a file
def load_from_file(path:str) -> list:
    output = []
    printv("---\nLOADING FILE FROM",path)
    # checking if file exists
    if not os.path.isfile(path):
        printv("ERROR: INPUT GIVEN IS NOT A FILE")
        return output 
    # trying to load file text
    try:
        with open(path,"r") as file:
            file_r:str = str(file.read())
            output = file_r.split(",")
    except:
        printv("ERROR: FILE NOT VALID")
        return output
    # outputting output
    printv("FILE READ SUCCESSFULLY")
    return output


# literally just random.choice(), but it tries to run the file
def surprise_me(list_input) -> str:
    printv("---\nSTARTING THE SELECTION")
    output = random.choice(list_input)
    printv(output, "SELECTED!")
    printv("RUNNING FILE...")
    # thank you Leo N from StackOverflow
    if platform.system() == "Windows":
        os.startfile(output)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, output])
    printv("SUCCESS!")
    return output
    



# test
def test():
    global verbose
    verbose = True
    input("HIT ENTER TO START INDEXING")
    current_index = perform_search("/home/jabble/Pictures/",True,(".png",".jpg",".jpeg",".mp4",".mov",".avi",".mkv",".wmv",".webm"))
    input("HIT ENTER TO SAVE FILE")
    save_to_file(current_index,"./test-output.csv")
    input("HIT ENTER TO LOAD FILE")
    loaded_index = load_from_file("./test-output.csv")
    while True:
        input("HIT ENTER TO SURPRISE ME!")
        surprise_me(loaded_index)


def main():
    test()



if __name__ == '__main__':
    main()            
