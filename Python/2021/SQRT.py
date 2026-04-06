def take_argument(list):
    while True:
        arg = input("Give a number. Keep giving numbers. When you are finished, type 'RUN'")
        try:
            arg = int(arg)
            list.append(arg)
        except:
            if arg.lower() == "run":
                break
            else:
                print("Please enter a number.")
                continue
    return list

def sqrt(arg,num):
    sqrtnum=arg**0.5
    print("SQARE ROOT OF ARG", str(arg) + "=", str(sqrtnum))
    return sqrtnum

def addnums(list):
    total=0
    for item in list:
        total+=item
    print("COMPLETE TOTAL IS", str(total))
    return total




list=[]
sqrtlist=[]

list=take_argument(list)
print("",end='\n')

loopcount=1
for item in list:
    sqrtlist.append(sqrt(item,loopcount))
    loopcount+=1

print("",end="\n")
print(sqrtlist)
addnums(sqrtlist)
input()