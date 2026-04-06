# This document contains useful functions I have created
# Hopefully in the future they will be organized somehow
# Maybe on number of parameters, return vs no return, etc.


#-----------------------------------------------------------------
#                         IMPORTS

import time
import random
import os


#----------------------------------------------------------------

# Prints a message letter by letter instead of all at once
# REQUIRED MODULE: time
def printf(message, *word, end = "\n", sep = " "):
    for letter in message:
        print(letter, end = '', flush = True)
        time.sleep(0.05)
    if word:
        for letter in word:
            print(letter, end = '', flush = True)
            time.sleep(0.05)
    else:
        pass
    if end == '':
        pass
    else:
        print("\n", end = '')
    return

# Takes a string, shuffles it, and returns it
# REQUIRED MODULE: random
def shuffle(string):
    import random

    string_temp = list(string)
    random.shuffle(string_temp)
    string_final = ''.join(string_temp)

    return string_final


# Clears the screen
# REQUIRED MODULE: os
def cls():
    import os

    os.system('cls' if os.name=='nt' else 'clear')
    return


# Prints elipses at a rate defined by the text speed (TS)
# TS by default is 1
TS = 1
#   Numbers > 1 = Slower Printing
#   Numbers < 1 = Faster Printing
# REQUIRED MODULE: time
def elip(TS):
    import time

    print(".", end = '', flush = True)
    time.sleep(.5 * TS)
    print(".", end = '', flush = True)
    time.sleep(.5 * TS)
    print(".", end = '', flush = True)
    time.sleep(1 * TS)
    return


# Replaces a specific line in a text file
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num - 1] = text
    with open(file_name, 'w') as out:
        out.writelines(lines)
    return

# Input function with built-in input validation
# Will continue to prompt the user for good input
# Expects a STRING from the user
def inputSTR(words = ''):
    while True:
        userIn = input(words)

        try:
            userIn = float(userIn)
        except:
            break
        else:
            print("\nInvalid Input - Please enter words, not numbers.")
            del userIn
            continue

    return

# Input function with built-in input validation
# Will continue to prompt the user for good input
# Expects a NUMBER (int or float) from the user
def inputNUM(words = ''):
    while True:
        userIn = input(words)

        try:
            userIn = float(userIn)
        except:
            print("\nInvalid Input - Please enter a number, not words.")
            del userIn
            continue
        else:
            break

    return

inputNUM("Please enter some numbers. ")