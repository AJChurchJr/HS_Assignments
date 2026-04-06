"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""

"""
-input a string
-make a dictionary { character : count }
-make another list, called "highest", that takes a list from the other list, although the default is ["",0]
-make a value, called "duplicate" ; a boolean that is False
-iterate through list 1:
--if the count is greater than the "highest" count, replace the list with that one and mark "duplicate" False
--if the count is equal to the "highest" count, mark "duplicate" True
-in the end, return None if "duplicate" is true, if not, return the "highest" count
"""

def string_mode(string_input=None):
    count = { }
    highest = [ "" , 0 ]
    duplicate = False

    #taking input if not present
    if string_input is None:
        string_input = input("Enter anything:")

    #counting letters
    for letter in string_input:
        if letter in count.keys():
            count[letter] += 1
        else:
            count[letter] = 1

    for key,value in count.items():
        #replacing highest if higher
        if value > highest[1]:
            highest = [key , value]
            duplicate = False
        #marking duplicate if equal
        elif value == highest[1]:
            duplicate = True

    if duplicate is not True: return highest
    else: return None
            
print(string_mode())

"""OUTPUTS:
"aa bb cc dd ee ff gg hh ii jj kk" : [ " " , 10 ]"
"abcdef" : None
"aabcdef": ["a":2]
[THE ENTIRE BEE MOVIE SCRIPT] : [" ",7798]

"""
