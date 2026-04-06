"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
def reset_files():
    if bool(input("Enter anything to rewrite test files test1 & test2:")):
        #rewrites the file with the original template text.
        opened_files = (open("./test1.txt","w"),open("./test2.txt","w"))
        info_to_write = (
"""Python is a great object-oriented, interpreted, and interactive
programming language. It is often compared (favorably of course :-) )
to Lisp, Tcl, Perl, Ruby, C#, Visual Basic, Visual Fox Pro, Scheme or Java...
and it's much more fun.""",
"""Welcome to the Python Wiki, a user-editable compendium of knowledge
based around the Python programming language. Some pages are protected
against casual editing - see WikiEditingGuidelines for more information
about editing content."""
)
        for i in range(len(info_to_write)):
            opened_files[i].write(info_to_write[i])
        for i in range(len(opened_files)):
            opened_files[i].close()

def splice_files(d1 = "./test1.txt", d2 = "./test2.txt"):
    #opening
    d1 = open(d1,"r");d2 = open(d2,"r")
    #splicing
    spliced = (d1.read(),d2.read())
    #closing
    d1.close();d2.close()
    return spliced
    
    
#actually running the code
def main():
    reset_files()
    output = splice_files()
    print(output)

if __name__ == "__main__":
    main()

    

"""OUTPUTS:
-Note for the past few files there have been no outputs since it writes to a file.
-I hope that makes sense.
"""
