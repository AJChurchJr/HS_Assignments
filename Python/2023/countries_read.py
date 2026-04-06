"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
file = open("./test.txt","a")
file_print = open("./test.txt","r"); print(file_print.read()); file_print.close ; del file_print
file.write(input("Enter a country to add:")+"\n") ; file.close()
file_print = open("./test.txt","r"); print(file_print.read()); file_print.close ; del file_print


