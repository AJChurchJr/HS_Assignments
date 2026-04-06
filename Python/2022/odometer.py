def iv(text):# makes an input statement and converts it to int with try-except
    while True:
        try:val=int(input(text)) ;break
        except: continue
    return val

odometer_start=iv("What is the first odometer reading?") #odometer start value
previous_mi=odometer_start #this is used to figure out the total amount of miles traveled
legs=[] #amount of legs used
tank=0 #tank gallon size
dist=0 #distance of road trip
gallons=0 #total gallons
miles=0 #total miles
mpg=0 #miles per gallon

curInp=input("Add new leg? (Y/N):") #starting for input loop
print("==========================")
while curInp.lower()=="y" or curInp.lower()=="yes":
    inp=iv("Current odometer reading?"),iv("Amount of gas used in leg?") #input
    if inp[0]<=previous_mi: print("The odometer cannot go down.");continue #input validation
    if inp[1]<=0: print("The gas mileage cannot be less than or equal to zero.");continue #input validation

    legs.append(inp)
    print("MILES USED IN LEG:",str(inp[0]-previous_mi),end=' \ ')
    print("GALLONS USED:",str(inp[1]),end=' | ')
    print("LEG MPG:", str((inp[0]-previous_mi)/inp[1]))

    #Once inp is all done being used, it is then transferred to previous_inp to check for odometer total status
    previous_mi=inp[0]

    curInp=input("Add new leg? (Y/N):") #checking if loop should repeat

    print("------------------------------")

print("==========================")
print("INITIAL ODOMETER:",str(odometer_start))
#for item in legs:print("LEG",str(legs.index(item)+1)+"|",str(item[0]-odometer_start),"MILES |",str(item[1]),"GALLONS") #debug prints
for item in legs:gallons+=item[1] #prints legs and makes a total amount of gallons
miles=max(legs)[0]-odometer_start
mpg=miles/gallons
print("TOTAL",str(miles), "MILES DRIVEN")
print("TOTAL",str(gallons),"GALLONS USED.")
print("AVERAGE",str(mpg),"MILES PER GALLON.")
print("==========================")
tank=iv("Gas tank size? (gal)")
dist=iv("Trip length? (mi)")
print("Your trip will take",str(dist/mpg),"gallons to complete your trip.")
print("Your trip will require", str((dist/mpg)/tank), " gas station stops.")






