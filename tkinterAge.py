import tkinter as tk
from tkinter import *
root = tk.Tk()
root.geometry("610x400")

age_label = Label(root, text = "Quel age as tu?")
age_label.place(x= 50,y= 50)

age_entry = Entry(root)
age_entry.place(x= 170,y= 50)

name_label = Label(root, text = "Quel est ton nom?")
name_label.place(x= 50,y= 80)

name_entry = Entry(root)
name_entry.place(x= 170, y= 80)


# etre sur que tous les name_entry valeurs sont en string
# etre sure que le nomqu'on entre est visuelle (on peut voir sur l'ecran)
def user_age():
    return_message = Label(root, text = "")
    valeur_input_box = int(age_entry.get())
    valeur_input_box_2 = name_entry.get()
    if 0 <= (valeur_input_box) and (valeur_input_box) < 2:
        return_message["text"] = "Bonjour " + str(valeur_input_box_2) + ", tu es un bébé"
        return_message.place(x= 50, y= 15)
    elif 2 <= (valeur_input_box) and (valeur_input_box) < 5:
        return_message["text"] = "Bonjour " + str(valeur_input_box_2) + ", tu es un toddler"
        return_message.place(x= 50, y= 15)
    elif 5 <= (valeur_input_box) and (valeur_input_box) < 12:
        return_message["text"] = "Bonjour " + str(valeur_input_box_2) + ", tu es un enfant"
        return_message.place(x= 50, y= 15)
    elif 12 <= (valeur_input_box) and (valeur_input_box) < 18:
        return_message["text"] = "Bonjour " + str(valeur_input_box_2) + ", tu es un adolescent"
        return_message.place(x= 50, y= 15)
    elif 18 <= (valeur_input_box) and (valeur_input_box) < 64:
        return_message["text"] = "Bonjour " + str(valeur_input_box_2) + ", tu es un adulte"
        return_message.place(x= 50, y= 15)
    elif int(valeur_input_box) > 64:
        return_message["text"] = "Bonjour " + str(valeur_input_box_2) + ", tu es un adulte âgé"
        return_message.place(x= 50, y= 15)

validation = Button(root, text = "validation", command = user_age)
validation.place(x= 50, y= 120)

root.mainloop()