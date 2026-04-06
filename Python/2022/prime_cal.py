from math import sqrt
def iv(text):# makes an input statement and converts it to int with try-except
    while True:
        try:val=int(input(text));break
        except: continue
    return val
def checkPrime(num):#CREDIT TO GEEKSFORGEEKS -- I KNEW THIS ALREADY BUT THEY FORMATTED IT BETTER
    if(num > 1):
        for i in range(2, int(sqrt(num)) + 1):#checking for any divisor
            if (num % i == 0):return False 
        return True
    else:return False
#for i in range(100):print(str(i),"|",str(check_if_prime(i)))

x=iv("Enter a number: ");sums=[];primeSums=[] #input, definitions
#adding all possible sums
for i in range(x):
    runnerUp=((i+1,x-(i+1)))
    if runnerUp in sums or (x-(i+1),i+1) in sums: continue #checking for duplicate inputs
    if x-(i+1)<=0:continue #checking for any +0 input
    sums.append(runnerUp)
    
for item in sums:
    flag=False #true means not prime, false means prime
    for num in item:
        if not checkPrime(num):flag=True
        else:pass
    if not flag:primeSums.append(item)
print("POSSIBLE:",str(sums))
print("PRIME:",str(primeSums))
    
