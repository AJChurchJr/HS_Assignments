"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
import random

"""PSEUDOCODE
-take input

-search for d, search for +
--if d is not present, crash
--if + is not present, make the "modifier" value 0

-take every index after +, as that will be the "modifier" value
--remove these indexes from the string
-take every index previous to d, as that will be the "dice number" value
--remove these indexes from the string
-take the leftover value and make it a value called "dice sides"
"""

def dice_range(roll = None):
    if roll is None:
        roll = input("enter a dice value")
    """default value declaration
    these are all used later"""
    roll=roll.lower()
    modifier = 0
    dice_number = 0
    dice_sides = 0

    """FIGURING OUT VALUES
    this is where it checks for d and + in order to assign values to the variables
    number first, modifier second, sides last
    """
    
    """checking for d"""
    if "d" in roll:
        if roll.index("d") == 0:
            """default argument"""
            dice_number = 1
        else:
            """checking every index before d to make the dice_number value"""
            dice_number = int(roll[:(roll.index("d"))])
        """getting rid of the value to make finding dice_sides easier"""
        roll = roll.replace(str(roll[:(roll.index("d")+1)]),"")
    else:
        """ERROR INPUT, there is no correct dice value"""
        return 0
    
    """checking for +-"""
    if ("+"in roll):
        modifier = int(roll[(roll.index("+")+1):])
        roll = roll.replace(str(roll[(roll.index("+")):]),"")
    elif ("-" in roll):
        modifier = int(roll[(roll.index("-")+1):])*-1
        roll = roll.replace(str(roll[(roll.index("-")):]),"")
    else:
        modifier = 0
        
    """assigning leftover to sides"""
    dice_sides = int(roll)
    del roll


    """FINALLY OUTPUTTING"""
    return random.randint(dice_number+modifier, (dice_sides*dice_number)+modifier)

input(dice_range())

    
"""OUTPUTS
print(dice_range("1d6")) [1,6]
print(dice_range("1d6+2")) [3,8]
print(dice_range("d6")) [1,6]
print(dice_range("d6-2")) [-1,4]
print(dice_range("2d6")) [2,12]
print(dice_range("2d6-1")) [1,11]
print(dice_range("0d6+1")) [1,1]
"""

