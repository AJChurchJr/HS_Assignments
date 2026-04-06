import time,random
class Game:
    def __init__(self):
        self.p1=[0,0];self.p2=[0,0] #0 is round score, 1 is total score
        self.turn=True; self.turns=0;self.over=False # current turn [t=p1,f=p2] / amount of turns / if game ended
        self.aggression=random.randint(2,10)#randomly selected aggression
    def round(self):
        self.turns+=1
        print("-----=====TURN",str(self.turns)+"=====-----")
        while self.turn==True: #player turn
            print("---YOUR turn!--- \nround:" + str(self.p1[0]) + "\ntotal:" + str(self.p1[1]))
            choice=input("a to roll, b to bank:");roll=0 #choice, along with resetting roll to prevent accidental application of previous round points
            if choice.lower()=='a':
                roll=random.randint(1,6)
                print("you rolled a " + str(roll) + "!")
                if roll==1: #code for emptying your round score and transferring turns
                    print("your turn is over\nturn given to P2")
                    self.p1[0]=0;self.turn=False;return
                self.p1[0]+=roll;del roll     
            elif choice.lower()=='b':
                print("earnings banked, turn given to P2")
                self.p1[1] += self.p1[0];self.p1[0] = 0 #empties round score into total score
                self.turn=False  
            else:
                print("earnings banked, turn given to P2")
                self.p1[1] += self.p1[0];self.p1[0] = 0 #empties round score into total score
                self.turn=False  
        while self.turn==False: #opponent turn
            print("---OPPONENT's turn!--- \nround:" + str(self.p2[1]) + "\ntotal:" + str(self.p2[0]))
            #print("turn given to P1");self.turn=True
            print("a to roll, b to bank:",end='')
            #how the ai works, the bot rolls between 1 and the aggression value
            #1 is the only value that means to bank
            #so the higher the aggression is, the less likely it is to bank
            #both options have their advantages
            if random.randint(1,self.aggression)==1:choice="b"
            else: choice="a"
            print(choice)#prints choice as if the opponent actually selected something
            if choice.lower()=='a':
                roll=random.randint(1,6)
                print("you rolled a " + str(roll) + "!")
                if roll==1: #code for emptying your round score and transferring turns
                    print("your turn is over\nturn given to P1")
                    self.p2[0]=0;self.turn=True;return
                self.p2[0]+=roll;del roll    
            elif choice.lower()=='b':
                print("earnings banked, turn given to P1")
                self.p2[1] += self.p2[0];self.p2[0] = 0 #empties round score into total score
                self.turn=True
            else:
                print("earnings banked, turn given to P1")
                self.p2[1] += self.p2[0];self.p2[0] = 0 #empties round score into total score
                self.turn=True
        #tallying character score and seeing if anyone is the victor
        if self.p1[1]>=100: print("=====\n====\n===\n==\n=Player 1 Wins!=\n==\n===\n====\n=====");self.over=True;return
        elif self.p2[1]>=100: print("=====\n====\n===\n==\n=Player 2 Wins=\n==\n===\n====\n=====");self.over=True;return
        else:self.over=False;return
game=Game()
while not game.over:game.round()
