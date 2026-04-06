"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""


"""
-function arguments:
--ball location (defaults to b)
--list containing all cup shifts (["ba","bc","ac"], etc.)

-iterate through all shifts
-if either cup has "ball" in it, swap balls with the other cup

"""

def cup_game(ball = "B" , shifts = []):
    #definitions
    all_cups = {"A":"","B":"","C":""}
    all_cups[ball] = "ball"
    answer=ball


    #shifting
    for shift in shifts:

        if "ball" in all_cups[shift[0]]:
            all_cups[shift[1]] = "ball"
            all_cups[shift[0]] = ""
            
        elif "ball" in all_cups[shift[1]]:
            all_cups[shift[0]] = "ball"
            all_cups[shift[1]] = ""



    #selecting answer
    for cup in all_cups.keys():

        if "ball" in all_cups[cup]:

            answer = cup

    #output
    return answer


print( cup_game( shifts=["BA", "AC", "CA", "BC"] ) )

"""OUTPUTS:
-["BA", "AC", "CA", "BC"] -> A
-["AB", "CA"] -> "C"
"""    
    
