"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
worda=input("Please enter a word: ").lower()
wordb=input("Please enter another word: ").lower()
#remove duplicate letters
worda_refined=""
wordb_refined=""
for letter in worda:
    if letter not in worda_refined:worda_refined+=(letter)
for letter in wordb:
    if letter not in wordb_refined:wordb_refined+=(letter)
print(worda_refined,wordb_refined)
#check for common letters
common_letters=[]
for letter in worda_refined:
    if letter in wordb_refined:
        common_letters+=letter
print(str(worda),"and",str(wordb),"have",str(len(common_letters)),"in common, sharing: ",end='')
for item in common_letters:print(item,end='')
