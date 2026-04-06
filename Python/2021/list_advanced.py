#1
def unique_items(listarg):
    existing_items=[]
    for item in listarg:
        if item in existing_items:
            continue
        else:
            existing_items.append(item)
    return existing_items
print(unique_items([1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,5,6,7,7,7,7,7,7,7,7,4,4,6,7,8,45]))

print("\n")

#2
#thanks to Kyle
def pascaltriangle(n):
    list=[]
    for i in range(n):
        list.append([])
        for j in range(i+1):
            if j == 0 or j == len(list[i-1]):
                list[i].append(1)
            else:
                list[i].append(list[i-1][j-1] + list[i-1][j])

    return list
def print_pascal(list):
    for item in list:
        print(item)
pascal=pascaltriangle(5)
print_pascal(pascal)

print("\n")

#3
def squarelist(min,max):
    list = []
    loopcount=min
    while True:
        list.append(loopcount**2)
        loopcount+=1
        if loopcount>max:
            break
    return list
print(squarelist(1,30))

print("\n")

#4
def multiplylist(list,multfactor):
    for i in range(len(list)):
        list[i]*=multfactor
    return list
print(multiplylist([1,2,3,4],5))

print("\n")

#5
def remove_odd(list):
    for item in list:
        if type(item) == int or type(item) == float:
            if item%2 != 0:
                list.remove(item)
    return list
print(remove_odd([1,2,3,4,5]))

print("\n")

#6
def list_index_remove(list):
    original_list=tuple(list)
    modified_list=list
    modified_list.pop(0);modified_list.pop(1);modified_list.pop(2)
    return (original_list,modified_list)
variable = list_index_remove([111,222,333,444,555,666,777,888,999,000])
print("ORIGINAL:",variable[0])
print("MODIFIED:",variable[1])

print("\n")

#7
def iterate(dictionary):
    for key,value in dictionary.items():
        print(str(key) + ":", str(value))
iterate({1:"Hello",2:"World",3:"!"})

print("\n")

#8
def random_tables(length):
    import random
    def rando():
        return random.randint(0,9)
    dict={}
    for i in range(length):
        dict["INDEX" + str(i)] = [rando(),rando(),rando()]
    return dict
def display_random_tables(dictionary):
    for key,values in dictionary.items():
        print(key + ":", end= "")
        for item in values:
            print(item,end=" ")
        print("\n")
display_random_tables(random_tables(10))

print("\n")

#9
def drop_empty(dictionary):
    for i in range(len(dictionary)):
        if dictionary[i+1]== None:
            dictionary.pop(i+1)
    return dictionary
print(drop_empty({1:None,2:"HELLO",3:None,4:"WORLD"}))
