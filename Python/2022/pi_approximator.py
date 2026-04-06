terms=None;cVal=1;total=0;curIter=True #cVal means current value; true means +, false means - on curIter
while type(terms)!=int:
    try:terms=int(input("==========PI APPROXIMATOR==========\nHow many processes?: "))
    except:continue
for i in range(terms):
    total=(total+(4/cVal)) if curIter else (total-(4/cVal))#modifying the total based off a turnary operator 
    cVal+=2;curIter=not curIter #swapping curIter and changing cVal
    print("CURRENT VALUE:",str(cVal),"| CURRENT ITERATION:",str(i),"| CURRENT TOTAL:",str(total)) #prints for displaying the value

