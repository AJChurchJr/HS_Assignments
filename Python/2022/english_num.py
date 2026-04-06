"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
###giving a list of all the english terms used
tensplace=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
ones=["","one","two","three","four","five","six","seven","eight","nine"]
hunthous=["","thousand","million","billion","trillion","quadrillion","kroogillion"]

print("Andrew Church - NO ERROR HANDLING - 2022")
###taking a number to enter - splitting into digits
num=input("Enter a number:")
numList=[[]]
current_list_used=0

#dividing number into bunches of three
for item in num:
    #makes a new bunch-of-three if the last one is full
    if len(numList[current_list_used])>=3:
        current_list_used+=1
        numList.append([])
    #adding item to the bunch-of-three
    numList[current_list_used].append(item)

for i in range(len(numList)):
    if len(numList[i]) < 3:
        for j in range(3-len(numList[i])):numList[i].insert(0,'0')
        
print(numList)
        

#turning every number into an integer instead of a string
for i in range(len(numList)):
    for j in range(len(numList[i])):numList[i][j]=int(numList[i][j])

#converting to english
englishList=[]
index=1
current_assembled_word=""
for item in numList:
    #handling the hundreds place. as this does not affect the tens place or the ones place, it runs individually
    if item[0]!=0:
        current_assembled_word+=(ones[item[0]]+" "+"hundred")
        current_assembled_word+=" "
    #handling the tens place. as this DOES affect the ones place, it needs to run as an if-else basis
    if item[1]!=0:
        #handles the teens
        if item[1]==1:current_assembled_word+=teens[item[2]]
        #handles any other tens place, along with the ones place
        else:
            current_assembled_word+=(str(tensplace[item[1]])+" "+str(ones[item[2]]))
        
        current_assembled_word+=" "
    #handling the ones place if the tens place goes unhandled
    else:
        current_assembled_word+=str(ones[item[2]])
        current_assembled_word+=" "
    
    current_assembled_word+=(hunthous[len(numList)-index] + ", ")
    index+=1
print(current_assembled_word)

"""
PSEUDOCODE
-take input for a number
-split list into three-digit chunks, REVERSED:
    -chunk digit 0 is the ones place
    -chunk digit 1 is the tens place
    -chunk digit 3 is the hundreds place
-give each chunk a name:
    -ones (no name)
    -thousands
    -millions
    -billions
    
"""
"""
OUTPUTS
1 - one
12 - twelve
123 - one hundred twenty three

"""
