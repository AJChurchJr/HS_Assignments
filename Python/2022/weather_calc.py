#Andrew Church
#Allen Krueger
#CIS AM
#Please note that I am not a fan of EVER hard-coding anything
#but I decided to do it here for the table since I would need to build an entire table system without stealing an import.
#this barely counts as "hard coding", it's just a table with pre-defined value
table={"keys":[-20,-10,0,10,20,30,40,50,60],0:[],5:[],10:[],15:[],20:[],25:[],30:[],35:[],40:[],45:[],50:[]}
v=0
for i in range(11):
    t=-20
    for j in  range(8):
        table[v].append(round((35.74 + (0.6215*t) - (35.75*(v**0.16)) + (0.4275*t*(v*0.16))),1))
        t+=10
    v+=5
for key,value in table.items(): print(str(key),"|",str(value))
