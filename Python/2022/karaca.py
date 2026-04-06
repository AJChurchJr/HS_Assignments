"""ANDREW CHURCH - ALLEN KRUEGR - CIS AM - INPUT apple - OUTPUT 1lpp0aca"""
#reverse input
#replace all vowels a=0 e=1 i=2 o=2 u=3
#add aca
word=input("Enter a word/phrase:");output=[];vowel={"a":0,"e":1,"i":2,"o":2,"u":3} #inputs, variables
for i in range(len(word)):output.append(word[len(word)-(i+1)]) #converting string to list & reversing it
for i in range(len(output)): output[i]=vowel[output[i]] if output[i] in vowel.keys() else output[i] #vowel conversion
tempstring="" #tempstring is just a temporary storage method 
for item in output: tempstring=str(tempstring)+str(item) #making tempstring final product
output=str(tempstring)+"aca" ; del tempstring #adding aca to the end, and making tempstring output, and deleting tempstring 
print(output)
