import time
import sys
from tkinter import *
import tkinter as tk
from tkinter import font

def temps():
    temps_presentement = time.strftime("%H:%M:%S")
    clock.config(text=temps_presentement)
    clock.after(200,temps)
    # retourne ici

root = tk.Tk()
root. geometry("500x500")
clock=Label(root, font=("times",50,"bold"), bg="red")
clock.grid(row=1,column=1,pady=10,padx=10)
temps()

root.mainloop()