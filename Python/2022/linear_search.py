"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
nums=input("INPUT a list of NUMBERS divided by SPACES: ").split(" ") #LIST CREATION
results=[] #Stored in a LIST [item,index,accuracy]
search=input("SEARCH: ") #SEARC

#main search
for i in range(len(nums)):
    if nums[i].lower()==search.lower(): results.append([nums[i],i,100]) #found at index i with 100% accuracy
#related search -- UNFINISHED
for i in range(len(nums)):
    lettermatch=0
    for letter in search:
        if letter in nums[i]:lettermatch+=1
    if lettermatch>0 and lettermatch/len(search)<=100: results.append([nums[i],i,((lettermatch/len(search))*100)])
        
print("--------------=RESULTS=--------------")     
for item in results:print(str(item[0]), "found at index", str(item[1]), "with accuracy", str(item[2])+"%")

