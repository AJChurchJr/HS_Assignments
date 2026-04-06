list1 = [1,2,3,4,5];list2 = [100,200,300,400,500]

if len(list1) == len(list2):
    for i in range(len(list2)):
        print(list1[i], end= " ")
        print(list2[(len(list2) - i) - 1])