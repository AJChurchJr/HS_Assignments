########################NESTED LIST APPENDING############################
# the list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]

for item in sub_list:
    list1[2][1][2].append(item)
print("exercise 1 final list:", str(list1))
#########################################################################

#################ADDING UNTIL SPECIFIED#################
#Needed module
import random
#The list
list1 = []
while True:
    #repeatedly adds a random number to the list and only stops when 3 is present
    list1.append(random.randint(1,10))
    if 3 in list1:
        list1.append("done.")
        break
print("exercise 2 final list:", str(list1))
########################################################

##################600 AFTER 500#####################
#The list
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list2 = []
dict = {}
for i in range(len(list1)):
    dict[i] = list1[i]
for key,value in dict.items():
    depth = 0
    if type(value) == list:
        while True:
            depth = 1
            for item in value:
                if item == 500:
                    value.append(600)
                    break
            break
for key,value in dict.items():
    list2.append(value)
print("exercise 3 final list:", str(list2))




