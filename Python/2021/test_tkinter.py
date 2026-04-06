from tkinter import *
import random
import time


def linecreate():
        for i in range(10):
                canvas.create_line(random.randint(0,300),random.randint(0,300),random.randint(0,300),random.randint(0,300),fill=random.choice(['red','blue','green','orange','yellow', 'purple']))
                


root=Tk()

b=Button(root, command=linecreate, text="click me")
b.pack()


canvas=Canvas(root, width=300, height=300, background='black')
canvas.pack()

mainloop()
