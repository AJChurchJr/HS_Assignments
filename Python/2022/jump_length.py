"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""

"""PSEUDOCODE
get values, get total moves, get event list 

Start at index 0
add the value of the list[index] to the index
add ("jumped", str(list[index]), "steps to position to index", str(index+str(list[index]))) to event list


if list[index] is 0, return false
elif list[index] > len(index), return false
elif conditionmet=True, return True
else: print panic 

"""

def jumpLength(lst=None):
    #INPUT
    if lst==None:
        lst=input("Enter a list of numbers, separated by commas:").split(",")
        for i in range(len(lst)):
            lst[i]=int(lst[i])
        index=0;turns=1;eventList=[];conditionMet=False

    #MAIN LOOP
    while index <= (len(lst)-1):
        #MOVING INDEX
        eventList.append(("TURN "+str(turns)+": Jumped "+str(lst[index])+" steps from index "+str(index)+" to index "+ str(index+lst[index])+str(".")))
        index+=lst[index];turns+=1

        #EXTRA EVENTS TO DETERMINE IF THE RETURN CONDITION HAS BEEN MET
        if index==(len(lst)-1):
            conditionMet=True
            eventList.append("Reached the end in "+str(turns)+" steps.");break
        elif index>(len(lst)-1):
            eventList.append("Impossible to reach last index: overjumped.");break
        elif lst[index]==0:
            eventList.append("Impossible to reach last index: 0 jump.");break
        elif index <0 :
            eventList.append("Impossible to reach last index: underjumped.");break
        elif turns>50:
            eventList.append("Impossible to reach last index: loop.");break

    #OUTPUT
    for item in eventList:print(item)
    return conditionMet

jumpLength()

"""OUTPUTS (what the function returns, not the print statements)
2,3,1,1,4: True
3,2,1,0,4: False
1,1,1,1,0: True
2,3,-1,0,0: True
"""
