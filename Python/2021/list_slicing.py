#Definitions
inputList = []
lenList = 0
lenOfThird = 0
ALLCHUNKS = {1:[],2:[],3:[]}
leftOver = []

#Takes input
inputList = list(input("Type anything and I will divide it into thirds:"))
lenList = len(inputList)

while True:
    #If the list is divisible by three, it will divide like normal.
    if len(inputList) % 3 == 0:
        lenOfThird = len(inputList) / 3
        break
    #The program takes extra precautions if there are one or two extra characters left over.
    elif len(inputList) % 3 == 1:
        #When I subtract the values at the end of the list, I have to subtract the number "len(inputList)" by 1.
        #This is because of the fact that list indexes start at 0 instead of 1.
        leftOver.append(inputList[len(inputList)-1])
        inputList.pop(len(inputList)-1)
    elif len(inputList) % 3 == 2:
        leftOver.append(inputList[len(inputList)-2])
        inputList.pop(len(inputList)-2)
        leftOver.append(inputList[len(inputList)-1])
        inputList.pop(len(inputList)-1)


#DIVIDING LIST CODE
loopcount = 0
currentChunk = 1
while True:
    #ACTUALLY APPENDING STUFF TO THE CHUNKS
    loopcount += 1
    ALLCHUNKS[currentChunk].append(inputList[loopcount-1])
    #CHECKING FOR A CHANGE OF CHUNKS
    if loopcount % lenOfThird == 0:
        currentChunk += 1
    if currentChunk >= 4:
        break

ALLCHUNKS["LEFTOVER"] = leftOver
print(ALLCHUNKS)

