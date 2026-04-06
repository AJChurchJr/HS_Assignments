#CODING ASSIGNMENT 3
#ANDREW CHURCH
#ADAM WALKER
#11/23/2020


#This defines what the functions that say what the equations do, so they will be performed once they're called.
def multiplication(num1, num2):
    product=(num1*num2)
    return product
def division(num1, num2):
    quotient=(num1/num2)
    return quotient
def addition(num1, num2):
    sum=(num1+num2)
    return sum
def subtraction(num1, num2):
    difference=(num1-num2)
    return difference
def exponent(num1, num2):
    result=(num1**num2)
    return result
def modulo(num1, num2):
    result=(num1%num2)
    return result
def floor(num1, num2):
    result=(num1//num2)
    return result

while True:
    
#This asks the user for two numbers, yelling at them if they enter a letter or symbol.
    while True:
        try:
            num1=input("Enter a first number: ")
            num1=float(num1)
        except ValueError:
            print("A number, you dimwit!")
            continue
        break
    while True:
        try:
            num2=input("Enter a second number: ")
            num2=float(num2)
        except ValueError:
            print("A number, you dimwit!")
            continue
        break
#This action asks the user what equation they would like to perform, and calls the corresponding variable.
    while True:
        equation=input("Would you like to add, subtract, multiply, divide, floor, modulo, or exponent?: ")
        if equation.lower()=="add":
            try:
                print(addition(num1, num2))
            except OverflowError:
                print("The result was too large! Please try again.")
            except:
                print("An error occured. You suck.")
            break
        if equation.lower()=="subtract":
            try:
                print(subtraction(num1, num2))
            except OverflowError:
                print("The result was too large! Please try again.")
            except:
                print("An error occured. You suck.")
            break
        if equation.lower()=="multiply":
            try:
                print(multiplication(num1, num2))
            except OverflowError:
                print("The result was too large! Please try again.")
            except:
                print("An error occured. You suck.")
            break
        if equation.lower()=="divide":
            try:
                print(division(num1, num2))
            except OverflowError:
                print("The result was too large! Please try again.")
            except ZeroDivisionError:
                print("YOU CANNOT DIVIDE BY ZERO.")
            except:
                print("An error occured, you suck.")
            break
        if equation.lower()=="exponent":
            try:
                print(exponent(num1, num2))
            except OverflowError:
                print("The result was too large! Please try again.")
            except:
                print("An error occured. You suck.")
            break       
        if equation.lower()=="floor":
            try:
                print(floor(num1, num2))
            except OverflowError:
                print("The result was too large! Please try again.")
            except:
                print("An error occured. You suck.")
            break
        if equation.lower()=="modulo":
            try:
                print(modulo(num1, num2))
            except OverflowError:
                print("The result was too large! Please try again.")
            except:
                print("An error occured. You suck.")
            break
        else:
            continue
       