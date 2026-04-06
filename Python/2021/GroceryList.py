import os,sys

grocery_items=['bread','milk','eggs','patrick','printer ink','air conditioner','spoon']
grocery_prices=[3.99,25,1.42,353.67,2000.75,30.23,40.30]
grocery_dict={}

try:
    for i in range(len(grocery_items)):
        grocery_dict[grocery_items[i-1]]=grocery_prices[i-1]
except:
    print("oops")

print("GROCERY LIST")
total = 0
for key,value in grocery_dict.items():
    print(key, "->", "$" + str(value))
    try:
        total += value
    except:
        print('oopsie')
print("\n")
print("Total:", "$" + str(total))
del grocery_items,grocery_prices,grocery_dict,total