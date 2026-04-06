import sys,os
choice=input("What number do you want a factorial of?")
try:
    choice = int(choice)
except:
    print("That was not a number.")
    sys.exit()
if choice < 0:
    print("No negatives allowed.")
    sys.exit()

num=choice
nextup=choice-1

while True:
    num*=(nextup)
    nextup-=1
    if nextup<=0:
        break
    else:
        continue
print("Your final number is:",str(num))