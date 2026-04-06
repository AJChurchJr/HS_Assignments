def SplitPrice(people,price,tippercent):
    tipmultiplier = 1 + (tippercent/100)
    pricePlusTip = price * tipmultiplier
    totalPerPerson = pricePlusTip/people
    return totalPerPerson
people = float(input("How many people are dining tonight?: "))
price = float(input("How much money is the meal?: "))
tippercent = float(input("How much are you tipping?: "))
totalPerPerson = SplitPrice(people,price,tippercent)
print("Each person would need to pay", int(totalPerPerson//1), "dollars and", int((totalPerPerson%1)*100), "cents")
