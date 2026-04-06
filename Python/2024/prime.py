import math,time
import os 

index = 0
totalprime = 0 
string_notprime = 0 
string_notprime_highest = 0 
while index < 1000000000000:
    try:        

        index += 1
        isprime = True
        for i in range(round(math.sqrt(index))):
            if i == 0 or i == 1:
                continue
            elif index % i == 0:
                isprime = False
                string_notprime += 1
                break
            else:
                continue
        
        if isprime:
            #raising total amount of nonprime numbers
            totalprime += 1
            #resetting nonprime string
            if string_notprime > string_notprime_highest:
                string_notprime_highest = string_notprime
            string_notprime = 0 
    except KeyboardInterrupt:   
        print(index,isprime,"||",totalprime,string_notprime,string_notprime_highest)
        

