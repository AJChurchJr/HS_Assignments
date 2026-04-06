list = [1,2,3,4,5,7,7,7,7,7,7,6,6,234,23,"lemon"]
def elementcount(list):
    elementDict = {}
    for item in list:
        if item in elementDict.keys():
            elementDict[item] += 1
        elif item not in elementDict.keys():
            elementDict[item] = 1
    return elementDict
print(elementcount(list))