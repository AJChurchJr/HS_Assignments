"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
#taking input
lst=input("Enter a list of numbers, divided by spaces: ").split(" ")
#finding minmax
highest,lowest=max(lst),min(lst)
#finding missing
missing=[]
while lowest<highest:
    lowest+=1
    if lowest not in lst:missing.append(lowest)
#output
if len(missing)==0: print("Your list is perfect.")
else:print(missing)


"""
OUTPUTS
1 2 3 4 5: Your list is perfect.
1 2 4 5: [3]
1 2 3 6 7: [4,5]
1: Your list is perfect
"""
