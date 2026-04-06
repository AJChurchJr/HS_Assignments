class CONTAINERVALUE:
    original_function:str = ""
    output:int = 0


while True:
    CONTAINERVALUE.original_function = input("ENTER IMPLICIT FUNCITON: ")
    
exec("CONTAINERVALUE.output = 129989184")
print(CONTAINERVALUE.output)


