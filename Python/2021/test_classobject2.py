#Andrew Church

import time
import random
import math

class Entity:
    #__init__ will define the health, attack, and defense, as well as maximums for all of those.
    #Thank you Jacob
    def __init__(self, name='placeholder', health=1, attack=1, defense=1,entitytype='entity',level=1,experience=0):
        #__init__ will define the health, attack, and defense, as well as maximums for all of those.
        #Thank you Jacob'
        self.name=name; self.health=health; self.attack=attack; self.defense=defense; self.entitytype=entitytype; self.level=level; self.experience=experience; self.maxhealth=10000; self.maxattack=500; self.maxdefense=500; self.minhealth=0
        if self.health>self.maxhealth:
            self.health=self.maxhealth
        if self.health<=self.minhealth:
            print("Why did you create a dead character?")
            self.health=0
        if self.attack>self.maxattack:
            self.attack=self.maxattack
        if self.defense>self.maxdefense:
            self.defense=self.maxdefense
    #repr just calls me stupid for trying to print a whole ass class
    def __repr__(self):
        return "DONT PRINT ENTITIES"

    #Damage will simply lower a character's health by however strong the hit was
    def Take_Damage(self, victim='placeholder', damage=1):
        print(victim.name, "took", damage, "damage!")
        victim.health-=damage

    #Attack will do the same, just slightly differently because somebody is doing the attacking.
    def Attack(self, victim):
        damage=self.attack - victim.defense
        if damage<0:
            print(self.name, "is too weak!")
        else:
            print(self.name, "hit", victim.name, "dealing", damage, "damage!")
            victim.health-=damage


    #Printstats does exactly what you think it does
    def PrintStats(self):
        print(self.name)
        print("TYPE:", self.entitytype)
        print("EXP:", self.experience)
        print("LVL:", self.level)
        print("HEALTH:",self.health)
        print("ATK:",self.attack)
        print("DEF:", self.defense)
    
    #Heal will go through your inventory (which might even be its own class!) and will ask you what item you would like to use.
    #This will also vary from entity to entity
    def Heal(self,inventory):
        #I have not done this yet, however
        pass


#Player will be the exact same as entity but will have a different method of attacking compared to an ENEMY
class Player(Entity):
    def GainExp(self,amount):
        print(self.name, "gained", str(amount), "experience!")
        self.experience+=amount
        while True:
            if self.experience>=self.level*10:
                self.LevelUp()
                self.experience-=self.level*10
                continue
            else:
                break
    def  LevelUp(self):
        self.level+=1
        self.defense+=0.25*self.defense
        self.attack+=0.25*self.attack
        self.health+=10
        self.defense=round(self.defense,2)
        self.attack=round(self.attack,2)
        self.health=round(self.health,2)
        print(self.name, "leveled up to level", str(self.level) + "!")
        print("DEF raised to", self.defense)
        print("ATK raised to", self.attack)
        print("HEALTH raised to", self.health)
        
        if self.health>self.maxhealth:
            self.health=self.maxhealth
        if self.attack>self.maxattack:
            self.attack=self.maxattack
        if self.defense>self.maxdefense:
            self.defense=self.maxdefense
            
class Enemy(Entity):
    pass
    




#-------------------------------------------------------------------

Jimmy=Player("Jimmy",2,2,22,'PLAYER')
Jimmy.GainExp(1000)
print('\n')
Jimmy.PrintStats()
input()

