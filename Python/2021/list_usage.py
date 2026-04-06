def listSum(list):
    num=0
    for item in list:
        if type(item) == int or type(item) == float:
            num += item
    return num
print(listSum([1,2,3]))
print(listSum([1,5,3,6,"sandwiches"]))

def stringReverse(string):
    string=list(string); dictionary={}; finishingstring=""
    for i in range(len(string)): dictionary[i] = string[i]
    dictlength=len(dictionary)-1
    for item in dictionary:
        finishingstring+=(dictionary[dictlength]);dictlength-=1
    return finishingstring
print(stringReverse("Hello"))

def mult_nums(num1,num2):
    total=0
    def add_nums(add1,add2):
        sum=add1+add2
        return sum
    for i in range(num2):
        total=add_nums(total,num1)
    return total
print(mult_nums(5,5))
print(mult_nums(30,5))

