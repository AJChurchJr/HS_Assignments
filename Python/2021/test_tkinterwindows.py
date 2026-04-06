import threading
import tkinter as tk
from tkinter import *
import time

window = tk.Tk()
window.geometry("500x500")


def thing():
    global font_size
    global something
    
    font_size = 25
    
    window2 = tk.Tk()
    window2.geometry("250x250")

    something = Label(window2, text = "shoot the baby", font = ("Arial", font_size))
    something.place(x = 250/2, y = 250/2, anchor = CENTER)

    th2 = threading.Thread(target = font_increase)
    th2.start()

    window2.mainloop()


    

def font_increase():
    font_size = 25
    while True:
        font_size += 1
        something.configure(font = ("Arial", font_size))
        time.sleep(0.5)

th1 = threading.Thread(target = thing)
th1.start()

window.mainloop()
