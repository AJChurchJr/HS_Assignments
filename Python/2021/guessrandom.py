import random,os,time,sys,random
#Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return
#Scroll prints
def printf(message, *word,speed, end = "\n",sep = " "):
    for letter in message:
        print(letter, end = '', flush = True)
        time.sleep(speed)
    if word:
        for letter in word:
            print(letter, end = '', flush = True)
            time.sleep(speed)
    else:
        pass
    if end == '':
        pass
    else:
        print("\n", end = '')
    return

#Globals out a lot of variables so they can be accessed easier.
global minimum,maximum,guesses_left,correctnumber,choice

#Allows you to select the difficulty of your game, and multiplies your maximum number by said number.
def select_difficulty():
    global minimum,maximum
    while True:
        cls()
        try:
            difficulty=int(input("On a scale of 1 to 10, what would you like your difficulty to be?"))
        except:
            continue
        minimum = random.randint(0,2*difficulty)
        maximum = random.randint(8*difficulty,10*difficulty)
        break

#This is where the program gives you hints depending on the number you guessed and the correct number.
def give_hints(correctnumber,choice=None,extrainfo=None):
    if extrainfo=="stringGiven":
        print("Hint: PUT A NUMBER. NOT WORDS!")
    if choice > correctnumber:
        print("Hint: Your guess is TOO HIGH!")
    if choice < correctnumber:
        print("Hint: Your guess is TOO LOW!")
    if correctnumber%choice==0:
        print("Hint: The correct number is DIVISIBLE by your guess!")
    if choice%correctnumber==0:
        print("Hint: Your guess is DIVISIBLE by the correct number!")
    if choice > correctnumber*2:
        print("Hint: Your guess is MORE THAN DOUBLE the correct number!")
    if choice*2 < correctnumber:
        print("Hint: The correct number is MORE THAN DOUBLE your guess!")
    
    
select_difficulty()
correctnumber=int(random.randint(minimum,maximum))
guesses_left=6
printf("I AM GUESSING A NUMBER BETWEEN ", str(minimum)," AND ", str(maximum),speed=0.01)

#And this is the meat and potatoes of the code. This is where the program repeatedly
#takes a guess and checks if it is correct or not, dropping a hint if you are wrong.
while True:
    if guesses_left>0:
        guesses_left-=1
        cls()
        #This try and accept program not only checks for your guess, but also throws an error in case if you were to input a word.
        try:
            printf("Guesses left:", str(guesses_left),speed=0.01)
            choice=int(input("GUESS:"))
            
        except:
            give_hints(correctnumber,choice=None,extrainfo="stringGiven")
            continue
        
        if choice == correctnumber:
            input("You guessed the number right!")
            break
        else:
            print("You did not guess the number correctly. Please try again.")
            give_hints(correctnumber,choice)
            input("Press enter to check again.")
            continue
    else:
        input("You have run out of guesses. GAME OVER.")
        break
        
print("END.")
