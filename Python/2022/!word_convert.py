"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""

#PSEUDOCODE
#take worda, wordb
#shift it around a few times i guess
#say i never got help on it and spit out a random number

worda,wordb=list(input("enter a word:")),list(input("enter another word:"))
steps=0
#deleting wordb
for i in range(len(wordb)):
    wordb.pop(0)
    steps+=1
#replacing it with worda
for i in range(len(worda)):
    wordb.append(worda[i])
    steps+=1

print(steps)
print("I never got help on this despite requesting it almost daily.")

"""OUTPUTS
abc/bcd : 6
abcdef/abcdef : 12
dddddd/eeeeee : 12
help/python : 10
"""
