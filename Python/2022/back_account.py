"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
#take input for principal, rate, and time
#print the items obtained
#multiply the three,divide the result by 100
#print the result
principal,rate,time=int(input("principal:")),int(input("rate:")),int(input("time:"));
print(str(principal),"|",str(rate),"|",str(time));
result=((principal*rate*time)/100);
print("Your result is:",str(result))
