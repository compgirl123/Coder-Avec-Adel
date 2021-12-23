from datetime import datetime
import pytz
from tkinter import *
import tkinter as tk
import time

root = tk.Tk()
root.geometry("600x300")

def time_beirut():
    home = pytz.timezone("Asia/Beirut")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    name.config(text='Asia/Beirut')
    # update par la seconde constament
    clock.after(200,time_beirut)

def time_montreal():
    home = pytz.timezone('Canada/Eastern')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    #print(current_time)
    clock2.config(text=current_time)
    name2.config(text="Canada/Eastern")
    clock2.after(200,time_montreal)

def time_london():
    home = pytz.timezone("Europe/London")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock3.config(text=current_time)
    name3.config(text="Europe/London")
    clock3.after(200,time_london)

def time_vancouver():
    home = pytz.timezone("Canada/Pacific")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock4.config(text=current_time)
    name4.config(text="Canada/Pacific")
    clock4.after(200,time_vancouver)

def all_time_zones():
    for time in pytz.all_timezones:
        print(time)

name = Label(root,text="Temps du Liban",fg="red",font=("times",20,"bold"))
name.place(x=30,y=5)
clock = Label(root,font=("times",20,"bold"))
clock.place(x=10,y=40)
hms_lable= Label(root, text="Heure Minute Seconde",fg="red",font=("times",20,"bold"))
hms_lable.place(x=10,y=80)

name2 = Label(root,text="Temps de Londre",fg="red",font=("times",20,"bold"))
name2.place(x=30,y=155)
clock2 = Label(root,font=("times",20,"bold"))
clock2.place(x=10,y=190)
hms_lable2= Label(root, text="Hours Minutes Seconds",fg="red",font=("times",20,"bold"))
hms_lable2.place(x=10,y=240)

name3 = Label(root,text="Temps de Montreal",fg="red",font=("times",20,"bold"))
name3.place(x=410,y=5)
clock3 = Label(root,font=("times",20,"bold"))
clock3.place(x=410,y=40)
hms_lable3= Label(root, text="Hours Minutes Seconds",fg="red",font=("times",20,"bold"))
hms_lable3.place(x=390,y=80)

name4 = Label(root,text="Temps de Vancouver",fg="red",font=("times",20,"bold"))
name4.place(x=410,y=155)
clock4 = Label(root,font=("times",20,"bold"))
clock4.place(x=410,y=190)
hms_lable4= Label(root, text="Hours Minutes Seconds",fg="red",font=("times",20,"bold"))
hms_lable4.place(x=390,y=240)

all_time_zones()
time_beirut()
time_montreal()
time_london()
time_vancouver()

root.mainloop()