"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
sentence=input("Please enter a sentence: ").split(" ");total_letters=0 #takes a sentence and splits it; creates a value for the total amount of letters
for item in sentence: total_letters+=len(item) #total amount of letters
print("Words in sentence:", str(len(sentence)), "| average word length in sentence:", str(round((total_letters/len(sentence)),1))) #prints the length of the sentence; prints the average length of the words

#INPUT: today is friday
#OUTPUT: 4.3
