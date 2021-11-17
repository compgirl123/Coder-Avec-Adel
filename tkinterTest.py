import tkinter as tk
parent_window = tk.Tk()
parent_window.title("test")
parent_window.geometry('200x200')
radio1 = tk.Radiobutton(parent_window, text ='premier', value = 1)
radio2 = tk.Radiobutton(parent_window, text ='deuxime', value = 2)
radio1.grid(column=0,row=0)
radio2.grid(column=1,row=0)