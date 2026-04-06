# Joseph Huber 
# Andrew Church
# Python



#DOCUMENTATION

#ISOLATING X - EVERYTHING DONE BUT DIVISION
#   -FIND THE SIDE WITH X INSIDE OF IT
#       -TAKE THE SIDE WITH X INSIDE OF IT AND THEN:
#           -IF THE TOTAL SIMPLIFIED NUMBER IS LABELED AS "ADD", IT WILL ADD [THE NUMBER MULTIPLIED BY -1] FROM THE OTHER SIDE, AND REPLACE THE ENTIRE LIST WITH JUST "X"
#           -IF THE TOTAL SIMPLIFIED NUMBER IS LABELED AS "MULT", IT WILL SUBTRACT THE NUMBER FROM THE OTHER SIDE, AND REPLACE THE ENTIRE LIST WITH JUST "X"

#DIVISION EQUATIONS WITH X PRESENT - UNFINISHED
#   -We plan to add support for division in the near future, but for now, if I were to plug it in like a module it would take days in order to be complete with it.
#   -Despite this, I have a few notes for when I *do* finish it.
#       -For every number that needs to be divided before X, you need to divide all of the numbers and it will work fine.
#           -EX: 10/5/x = 2/x
#       -For every number that needs to be divided after X, you need to multiply all of the numbers and it will work fine.
#           -EX: x/10/5 = x/50
#       -So, a full example would look like:
#           -10/5/x/10/5 = 2/x/50

#"COMPLEX" EQUATIONS - UNFINISHED
#   -Some equations are marked in their index as "complex" equations.
#   -Within these complex equations, the list that contains the numbers also contains other lists
#   -The lists being marked as "complex" allows the computer to know not to interact with them because the word "complex" is not registered
#   -This is for later

#NEGATIVE ISSUE - UNFINISHED
#   -There is currently a glitch within the python file with negative numbers that are the first index on either side of the equals sign.
#   -If a negative is detected, the entire problem appears to switch sides and attach to whatever the first thing it detects is.
#   -I do not have a fix for the issue but soon enough it will be in the works.




#SUBTRACTION ISSUE - FIXED
#   -Cannot finish subtraction without a complete rework of the "format_equation" function.
#      -I must convert all numbers to negatives and simply format them within "add"

#SIMPLIFYING SIDE WITHOUT X - FINISHED
#   -CONVERT THE OTHER SIDE TO *JUST* A NUMBER THROUGH SIMPLIFICATION MEANS.
#       -IF THE NUMBER IS SIMPLIFIED TO THE TRUEST POINT AND IS A SINGULAR NUMBER LABELED AS "ADD", THE PROGRAM WILL DO NOTHING BUT CONVERT THAT ENTIRE UNIT TO A SINGULAR NUMBER.
#       -THIS MAKES IT EASIER TO MULTIPLY, DIVIDE, ADD, AND SUBTRACT WHILE ISOLATING X




def take_input():
    equateUnsolved = input("Input an X-VARIABLE equation: ")
    equateUnsolved = list(equateUnsolved)
    for item in equateUnsolved:
        if item == " " or item == "":
            equateUnsolved.remove(item)
    return equateUnsolved

def check_syntax(equateUnsolved): 
    #DEFINITIONS NEEDED
    requirements = { "hasEquals": False , "hasX": False, "onlyOneVar" : None , "noZeroDivide": None , "noLoneModifiers" : None , "onlyOneEq" : False}
    varAppear = 0
    eqAppear = 0
    varInUse = None
    alphabetList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    #ITERATES FOR EVERY ITEM INSIDE OF EQUATEUNSOLVED
    for i in range(len(equateUnsolved)):
        
        #CHECKING FOR EQUALS SIGN
        if equateUnsolved[i] == "=":
            requirements["hasEquals"] = True
            eqAppear += 1
            if eqAppear > 1:
                requirements["onlyOneEq"] = False
        if eqAppear <= 1:
            requirements["onlyOneEq"] = True
            
        #CHECKING FOR VARIABLE AMOUNT
        if equateUnsolved[i].lower() in alphabetList:
            if varInUse == None:
                varAppear +=1
                varInUse = equateUnsolved[i]
            elif varInUse == equateUnsolved[i]:
                pass
            else:
                varAppear += 1
            if varAppear == 1:
                requirements["hasX"] = True
                requirements["onlyOneVar"] = True
            elif varAppear < 1:
                requirements["hasX"] = False
                requirements["onlyOneVar"] = False
            elif varAppear > 1:
                requirements["hasX"] = True
                requirements["onlyOneVar"] = False
        else:
            if requirements["onlyOneVar"] != False:
                requirements["onlyOneVar"] = True
                
        #CHECKING FOR LONE MODIFIERS
        if equateUnsolved[i] == "*" or equateUnsolved[i] == "/" or equateUnsolved[i] == "+" or equateUnsolved[i] == "-":
            try:
                if equateUnsolved[i+1] == "=":
                    requirements["noLoneModifiers"] = False
                else:
                    requirements["noLoneModifiers"] = True
            except:
                requirements["noLoneModifiers"] = False
        else:
            if requirements["noLoneModifiers"] != False:
                requirements["noLoneModifiers"] = True
            else: pass
        
        #CHECKING FOR ZERO DIVIDE
        if equateUnsolved[i] == "/":
            if equateUnsolved[i+1] == "0":
                requirements["noZeroDivide"] = False
        else:
            if requirements["noZeroDivide"] == False:
                pass
            else:
                requirements["noZeroDivide"] = True

            
            
    for value in requirements.values():
        if value == True:
            continue
        elif value == False:
            if requirements["hasEquals"] == False:
                print("No Equals Sign Detected. Please Re-Enter.")
            if requirements["hasX"] == False:
                print("No Variables Detected. Please Re-Enter.")
            if requirements["onlyOneVar"] == False:
                print("More Than One Variable Detected. Please Re-Enter.")
            if requirements["noZeroDivide"] == False:
                print("DIVIDE BY ZERO detected. Please Re-Enter.")
            if requirements["noLoneModifiers"] == False:
                print("Lone Modifier Detected. Please Re-Enter.")
            if requirements["onlyOneEq"] == False:
                print("Multiple Equals Signs Detected. Please Re-Enter.")
            return False
    return True
           
def format_equation(equation):
    numList = [0,1,2,3,4,5,6,7,8,9]
    numListString = ["0","1","2","3","4","5","6","7","8","9"]
    alphabetList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    #LOWERCASES VARIABLE FOR EASIER CODE MANAGEMENT
    for i in range(len(equation)):
        if equation[i].lower() in alphabetList:
            equation[i] = "x"
    
    #MERGING SEVERAL-DIGIT NUMBERS
    for i in range(len(equation)):
        hasFinished = False
        try:
            if equation[i] in numListString and equation[i+1] in numListString:
                baseIndex = i
                equation[i] = equation[i] + equation[i+1]
                equation.pop(baseIndex + 1)
                
                while True:
                    if hasFinished == False:
                        for i in range(len(equation)):
                            if equation[baseIndex + 1] in numListString:
                                equation[baseIndex] = equation[baseIndex] + equation[baseIndex + 1]
                                equation.pop(baseIndex + 1)
                                break
                            else:
                                hasFinished = True
                                break
                    elif hasFinished == True:
                        break
            else: continue
        except:
            break

    #CONVERTING NUMBERS TO INT AND KEEPING OTHERS AS STRINGS
    for item in equation:
        for i in range(len(equation)):
            try: equation[i] = int(equation[i])
            except: continue

    #CREATING NEGATIVES AND SIMPLY MAKING THEM "ADD"
    for item in equation:
        for i in range(len(equation)):
            if equation[i] == "-":
                equation[i+1] *= -1
                equation[i] = "+"

    #MERGING SEVERAL-NUMBER MULTIPLIERS
    #Quick thing to note with numbers converted by their modifiers.
    #   A number that is turned into a list is formatted as such:
    #       [(list of numbers),(type of equation that is modifying them)]
    def merge_modifiers(arg,arg2):
        hasFinished = False
        for i in range(len(equation)):
            hasFinished = False
            try:
                if equation[i] == arg or equation[i] == arg2:
                    argUsed = equation[i]
                    baseIndex = i-1
                    equation[baseIndex] = [[equation[baseIndex],equation[baseIndex + 2]]]
                    equation.pop(baseIndex+1)
                    equation.pop(baseIndex+1)
                    while True:
                        if hasFinished == False:
                            for i in range(len(equation)):
                                try:
                                    if equation[baseIndex + 1] == argUsed:
                                        equation[baseIndex][0].append(equation[baseIndex+2])
                                        equation.pop(baseIndex + 1); equation.pop(baseIndex + 1)
                                        break
                                    else:
                                        if argUsed == "*": equation[baseIndex].append("mult")
                                        if argUsed == "/": equation[baseIndex].append("div")
                                        if argUsed == "+": equation[baseIndex].append("add")
                                        if argUsed == "-": equation[baseIndex].append("subtract")
                                        hasFinished = True
                                        break
                                except:
                                    if argUsed == "*": equation[baseIndex].append("mult")
                                    if argUsed == "/": equation[baseIndex].append("div")
                                    if argUsed == "+": equation[baseIndex].append("add")
                                    if argUsed == "-": equation[baseIndex].append("subtract")
                                    hasFinished = True
                                    break

                        elif hasFinished == True:
                            break
                        else: continue
            except:
                break
        return equation
    equation = merge_modifiers("*","/")
    equation = merge_modifiers("+","+")
    for i in range(len(equation)):
        if equation[i] in alphabetList:
            equation[i] = ["x","LONE VARIABLE"]
            break

    #The final thing the program will check is for lone modifiers, which it will then delete.
    for item in equation:
        if item == "-" or item == "+" or item == "*" or item == "/":
            equation.remove(item)

    #SPLITTING THE EQUATION INTO TWO SIDES
    equateLeft = []
    equateRight = []
    for i in range(len(equation)):
        if i < equation.index("="):
            equateLeft.append(equation[i])
        elif i > equation.index("="):
            equateRight.append(equation[i])
        elif i == equation.index("="):
            continue

    equateFull = (equateLeft,equateRight)
    return equateFull

#SIMPLIFYING EQUATIONS BY MERGING THE SEVERAL-NUMBER LISTS
def simplify_equation(equation):
    for item in equation:
        itemIndex = equation.index(item)
        #MERGING EVERY SINGLE ITEM INSIDE OF A LIST THAT DOES NOT CONTAIN X
        if type(item) == list and type(item[0]) == list and "x" not in item[0]:
            if item[1] == "add":
                trueSum = 0
                exceptionList = []
                for item in item[0]:
                    if type(item) != list:
                        trueSum+=item
                    else:
                        exceptionList.append(item)
                if len(exceptionList) > 0:
                    exceptionList.insert(0,trueSum)
                    item = [exceptionList, "ComplexAdd"]
                else:
                    item = [trueSum, "add"]
                equation[itemIndex] = item
            if item[1] == "mult":
                trueSum = 1
                exceptionList = []
                for item in item[0]:
                    if type(item) != list:
                        trueSum *= item
                    else:exceptionList.append(item)
                if len(exceptionList) > 0:
                    exceptionList.insert(0,trueSum)
                    item = [exceptionList, "ComplexMult"]
                else:item = [trueSum, "add"]
                equation[itemIndex] = item
            if item[1] == "div":
                trueSum = item[0][0]
                print(trueSum)
                exceptionList = []
                for i in range(len(item[0])):
                    if type(item[0][i]) != list:
                        try:
                            trueSum /= item[0][i+1]
                        except IndexError:
                            continue
                    else:print('EXCEPTIONS OCCURED'); exceptionList.append(item)
                if len(exceptionList) > 0:
                    exceptionList.insert(0,trueSum)
                    item = [exceptionList,"ComplexDiv"]
                else: item = [trueSum, "add"]
                equation[itemIndex] = item
        #DOES THE SAME EXCEPT WITH SOME ACTIONS FOR IF X IS PRESENT
        elif type(item) == list and type(item[0]) == list and "x" in item[0]:
            if item[1] == "add":
                trueSum = 0
                exceptionList = []
                item[0].remove("x")
                item[0].insert(0,"x")
                for i in range(len(item[0])):
                    if type(item[0][i]) != list:
                        try:
                            trueSum += item[0][i+1]
                        except IndexError:
                            continue
                    else: exceptionList.append(item)
                if len(exceptionList) > 0:
                    exceptionList.insert(0,trueSum)
                    exceptionList.insert(0,"x")
                    item = [exceptionList, "ComplexAdd"]
                else:
                    item = [["x", trueSum], "add"]
                equation[itemIndex] = item
            elif item[1] == "mult":
                exceptionList = []
                item[0].remove("x")
                item[0].insert(0, "x")
                trueSum = item[0][1]
                for i in range(len(item[0])):
                    if type(item[0][i]) != list:
                        try:
                            trueSum *= item[0][i + 2]
                        except IndexError:
                            continue
                    else:
                        exceptionList.append(item)
                if len(exceptionList) > 0:
                    exceptionList.insert(0, trueSum)
                    exceptionList.insert(0, "x")
                    item = [exceptionList, "ComplexMult"]
                else:
                    item = [["x", trueSum], "mult"]
            elif item[1] == "div":
                pass
            equation[itemIndex] = item
    return equation


#FINDING MODIFIERS WITH X INSIDE OF IT AND THEN SWAPPING WITH THE OTHER SIDE.
def swap_sides(leftside,rightside):
    sideWithX=None
    #CHECKING FOR WHICH ITEM HAS X
    for item in leftside:
        if type(item) == list and "x" in item:
            sideWithX = "left"
        if type(item) == list and type(item[0]) == list and "x" in item[0]:
            sideWithX = "left"
        if item == "x":
            sideWithX = "left"
    for item in rightside:
        if type(item) == list and "x" in item:
            sideWithX = "right"
        if type(item) == list and type(item[0]) == list and "x" in item[0]:
            sideWithX = "right"
        if item == "x":
            sideWithX = "right"

    #SIMPLIFYING THE SIDE THAT DOES NOT CONTAIN X
    def simplifyOther(side):
        for item in side:
            itemIndex = side.index(item)
            if type(item) == list:
                if item[1] == "add":
                    side = item[0]
        return side
    if sideWithX == "left":
        rightside = simplifyOther(rightside)
        if type(rightside) == list:
            rightside = rightside[0]
        else:
            pass
    elif sideWithX == "right":
        leftside = simplifyOther(leftside)
        if type(leftside) == list:
            leftside = leftside[0]
        else:
            pass


    #CONVERTING ADDITION STATEMENTS WITH X INSIDE TO THE OTHER SIDE
    #If you check the simplify_equation section, if X is in the equation, the program automatically moves x to the first index of the list
    #   the number being added to x gets put in the second index of the list.
    #Knowing this, all I need to do is subtract the second number of the list on both sides.
    if sideWithX == "left":
        for item in leftside:
            if type(item) == list and item[1] == 'add' and item[0][0] == "x":
                rightside -= item[0][1]
                leftside[leftside.index(item)] = "x"
            if type(item) == list and item[1] == 'mult' and item[0][0] == "x":
                rightside /= item[0][1]
                leftside[leftside.index(item)] = "x"

    if sideWithX == "right":
        for item in rightside:
            if type(item) == list and item[1] == 'add' and item[0][0] == "x":
                leftside -= item[0][1]
                rightside[rightside.index(item)] = "x"
            if type(item) == list and item[1] == 'mult' and item[0][0] == "x":
                leftside /= item[0][1]
                rightside[rightside.index(item)] = "x"


    if sideWithX == "left" and "x" in leftside and len(leftside) == 1:
        leftside = "x"
    if sideWithX == "right" and "x" in rightside and len(rightside) == 1:
        rightside = "x"
    return((leftside,rightside))




while True:
    equateUnsolved = take_input()
    syntax = check_syntax(equateUnsolved)
    if syntax == False:
        continue
    elif syntax == True:
        pass
    equateUnsolved = format_equation(equateUnsolved)
    leftside = equateUnsolved[0]
    rightside = equateUnsolved[1]
    leftside = simplify_equation(leftside); rightside = simplify_equation(rightside)
    answer_tuple = swap_sides(leftside,rightside)
    print(str(answer_tuple[0]) + "=" + str(answer_tuple[1]))


    
    
