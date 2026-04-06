#DEFINING EVERYTHING
list_a = [0,1,2,3,4,5,6,7,8,9]
list_a_odds = []
list_b = [10,11,12,13,14,15,16,17,18,19]
list_b_evens = []
lists_merged = []
lists_stacked = []

#GATHERING ODDS FROM A AND EVENS FROM B
for i in range(len(list_a)):
    if i % 2 == 1:
        list_a_odds.append(list_a[i])
for i in range(len(list_b)):
    if i % 2 == 0:
        list_b_evens.append(list_b[i])

print("Original List Given:", str(list_a))
print("Modified List Odds:", str(list_a_odds))

print("Original List Given:", str(list_b))
print("Modified List Evens:", str(list_b_evens))


#STACKING THE EVEN LISTS AND ODD LISTS
lists_stacked = list_a_odds + list_b_evens
print("Lists stacked back-to-back:", str(lists_stacked))


#MERGING THE LISTS TOGETHER SO THEY'RE BACK IN THEIR EVEN-ODD ORDER
if len(list_b_evens) == len(list_a_odds):
    for i in range(len(list_a_odds)):
        lists_merged.append(list_b_evens[i])
        lists_merged.append(list_a_odds[i])
print("Lists merged together by index:",str(lists_merged))


