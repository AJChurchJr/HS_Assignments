"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
#taking input -- merging and sorting
lst=input("enter a list of numbers, separated by spaces:").split(" ")+input("do it again:").split(" ")
#input validation
i=0
while i<len(lst)-1:
    for i in range(len(lst)):
        try:lst[i]=int(lst[i])
        except:lst.pop(i);break
#sorting list as numbers
lst.sort()
#solving 
middle=len(lst)/2 #first it gives the actual index number
if middle%1>0:median=lst[int(middle-0.5)]#odd number code
elif middle%1==0:median=(lst[int(middle-1)]+lst[int(middle)])/2#even number code
else: median="ERROR"#exception
print("Your median is",str(median))
"""
OUTPUTS:
1 2 3 4 5 6 + 7 8 9 : Your median is 5.0
1 2 3 4 5 6 7 8 9 : Your median is 5.0
1 2 3 4 5 6 7 + 8 : your median is 4.5
1 2 3 4 + 7 8 : your median is 3.5
1 2 3 4 5 + 111 222 333 444 555 : Your median is 58.0
"""
