"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
from math import sqrt
#CODE PULLED FROM OLD ASSIGNMENT
def checkPrime(num):#CREDIT TO GEEKSFORGEEKS -- I KNEW THIS ALREADY BUT THEY FORMATTED IT BETTER
    if(num > 1):
        for i in range(2, int(sqrt(num)) + 1):#checking for any divisor
            if (num % i == 0):return False 
        return True
    else:return False
    
def nextPrime(num=None):
    #takes input
    if num is None: num=int(input("Enter a number:"))
    #if the number isn't prime, it repeatedly raises the number by 1
    if not checkPrime(num):
        while True:
            num += 1
            #if the new number is prime it returns
            if checkPrime(num):
                return num
    #if the number is already prime
    else:
        return num

print(nextPrime())

"""OUTPUTS:
1 -> 2
2 -> 2
1000 -> 1009
"""
