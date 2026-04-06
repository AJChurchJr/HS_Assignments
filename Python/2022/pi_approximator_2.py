"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM""" 
"""CREDIT TO JADYN FOR ASSISTANCE"""
import random,math
def iv(text):# makes an input statement and converts it to int with try-except
    while True:
        try:val=int(input(text));return val
        except: continue    
N=iv("How many darts? ");M=0
for i in range(N):
    pos = (random.uniform(0,1),random.uniform(0,1))
    dist = math.sqrt((pos[0]**2)+(pos[1]**2))
    if dist<=1:M+=1
    print(str(i),str(4*M/N),str(pos),str(dist),str(M))
print("Pi is: ",str(4*M/N))
