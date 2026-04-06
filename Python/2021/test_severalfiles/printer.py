from tkinter import *
import time
import threading


def read():
    while True:
        with open("value.txt",'r') as v:
            printer=v.read()
        print(printer)
        time.sleep(0.5)
        
def write():
    while True:
        with open("value.txt","r") as v:
            value=v.read()
            value=int(value)
        with open("value.txt","w") as v:
            value+=1
            v.write(str(value))
        print("File written.")
        time.sleep(0.5)
def openpython():
    exec(open("test1.py").read())
def openpython2():
    exec(open("test2.py").read())

        
th1=threading.Thread(target = openpython)
th1.start()

th2=threading.Thread(target = openpython2)
th2.start()
