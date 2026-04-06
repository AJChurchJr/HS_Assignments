from math import sqrt
import time
a = b = 0
c1 = []
c2 = []
comparison = []
abc = 0
time1 = time2 = 0 

#real sqrt
start = time.time()
for i in range(1000):
    a = i + 1
    for j in range(1000):
        b = j + 1
        c1.append(sqrt(a**2 + b**2))
end = time.time()
time1 = round(end-start,5)

#alternate sqrt
start = time.time()
for i in range(1000):
    a = i + 1
    for j in range(1000):
        b = j + 1
        c2.append(a + ((.5*(b**2))/a))
end = time.time()
time2 = round(end-start,5)

#comparision
for i in range(len(c1)):
    comparison.append(c2[i]/c1[i])
abc = sum(comparison)/len(comparison)
    



print(abc, "margin of error.")
input(str(time1) + " || " + str(time2))
