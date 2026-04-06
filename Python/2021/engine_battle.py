#required imports.
import time
import os
import winsound
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return
health=100
def battle_mechanics(bossname="Joe Biden",bosshealth=10,attack=10, health=10):
    print(bossname + " attacks!")
    print("Max health:" + str(bosshealth))
    print("Attack:" + str(attack))
    time.sleep(1)
    while True:
        if bosshealth<=0:
            print(bossname + " was defeated!")
            time.sleep(1)
            break
        if health<=0: 
            print("You died!")
            time.sleep(1)
            break
        print("Boss Health:" + str(bosshealth))
        print("Your Health:" + str(health))
        print("What will you do?\n1.Attack\n2.heal?")
        yourturn=input()
        if yourturn=="1" or yourturn.lower()=="attack":
            print("You throw a punch at " + bossname +", dealing 2 damage!")
            time.sleep(1)
            bosshealth=bosshealth-2
        elif yourturn=="2" or yourturn.lower()=="heal":
            print("You ate McDonalds. 10 health healed.")
            health=health+10
            time.sleep(1)
        else:
            print("For not inputting correctly, your turn gets skipped.")
        bossdamage=random.randint(1,int(attack))
        print(bossname + "throws his fists at you, dealing " + str(bossdamage) + " damage!")
        health=health-bossdamage
        time.sleep(1)
        input("Press enter to continue")
        cls()
        continue
battle_mechanics()

