#Andrew Church
#Mr. Kreuger
#Year 2
#11/1/21

#LIST REVERSING
def listreverse(list):
    list.reverse()
    return list
print(listreverse(["a","b","c","d","e","f"]))

print('\n')

#DOUBLING IN SIZE PER ITERATION
def sizedouble(argument,length):
    list = [argument]
    counter = 1
    for i in range(length):
        for i in range(counter):
            list.append(argument)
        print(list)
        counter *= 2
    del counter,list
sizedouble("a",5)

print('\n')


