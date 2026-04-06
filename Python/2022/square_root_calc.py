"""
Andrew Church
Allen Krueger
CIS AM
Outputs are shown in the code.
"""
import math #FOR TEST PURPOSES
arg=None;guess=None;total=0;acc="NULL";iterations=0 #definitions, all are self-explanatory
print("==========SQRT APPROXIMATOR==========")
while type(arg)!=int or type(guess)!=int or guess==0: #taking inputs, all are self-explanatory
    try:
        arg=int(input("NUM TO CALCULATE:"))
        guess=int(input("GUESS:"))
    except:continue
while acc!=100.00: #repeats until accuracy is 100
    iterations+=1 #iterations
    acc=((guess/math.sqrt(arg))*100) #accuracy percent
    print("ARG ",str(arg),"| ITERATION",str(iterations),"| CURRENT GUESS",str(guess),"| ACCURACY",str(acc)+"%") #displaying current items
    guess=(guess+(arg/guess))/2 #guess algorithm
print("TASK COMPLETED IN ",str(iterations),"ATTEMPTS.") #end display
        
