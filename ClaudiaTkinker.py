import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
from tkinter.ttk import Progressbar

# La fenetre du programme:
parent_window = tk.Tk()
parent_window.title('Le programme de Adel')
#frame = tk.Frame(parent_window)
#frame.pack()
my_description = tk.Text(parent_window)

def test():
    #Text Widget
    my_description.insert('1.0',"Cela est un programme Python")
    my_description.insert('1.4',"Test de ordre")
    # enlever le c de la fenetre
    my_description.delete('1.0')

def user_inputs():
    # Description de ce qu'on veut entrer
    username = tk.Label(parent_window,text = "Nom").place(x=10,y=50)
    # Place ou on peut entrer des donees
    entree_username = tk.Entry(parent_window).place(x=50,y=50)

    # Email
    email = tk.Label(parent_window,text="Email").place(x=10,y=90)  
    # input
    entree_email = tk.Entry(parent_window).place(x=50,y=90)

    # Password (a faire par adel)
    password = tk.Label(parent_window,text="Password").place(x=10,y=130)

    entree_password = tk.Entry(parent_window).place(x=77,y=130)

    # bouton pour soumettre l'information au serveur
    bouton_soumission = tk.Button(parent_window, text="Submit",activebackground ="black",activeforeground = "white").place(x=200,y=200)

def radiobuttons():
    # Creation d'une liste avec des boutons radio
    # mettre 4 valeurs pour selectionner.
    parent_window.title("Radio button")
    option1 = tk.Radiobutton(parent_window,text='Option1',value=1)
    option2 = tk.Radiobutton(parent_window,text="Option2",value=2)
    option3 = tk.Radiobutton(parent_window,text="Option3",value=3)
    option4 = tk.Radiobutton(parent_window,text="Option4",value=4)
    option1.place(x=0,y=0);
    option2.place(x=0,y=20);
    option3.place(x=0,y=40);
    option4.place(x=0,y=60);

def canvas():
    # creation d'un canvas en tkinter
    canvas_width = 500
    canvas_height = 500
    totale = tk.Canvas(parent_window,width=canvas_width,height=canvas_height)
    totale.pack()
    creation_ligne = int(canvas_height/2)
    totale.create_line(0,creation_ligne,canvas_width,creation_ligne,fill="#FFFFFF")

# creation d'un titre avec description dans l'application.


# creation d'une fonction qu'on va faire apparaitre sur l'ecran
def dire_allo():
    print("allo")

def bouton_allo():
    # creation des deux boutons avec Allo et Exit
    frame = tk.Frame(parent_window)
    frame.pack()
    bouton_allo = tk.Button(frame,text="Dire Allo",fg="red",command=dire_allo())
    bouton_allo.pack(side=tk.LEFT)

def bouton_exit():
    # creation d'un bouton en tkinter
    frame = tk.Frame(parent_window)
    frame.pack()
    bouton_exit = tk.Button(frame,text='Exit',command=quit)
    #bouton.pack()
    bouton_exit.pack(side=tk.RIGHT)

def checkbutton():
    # creation d'un checkbutton dans le GUI
    vrai_ou_faux = tk.BooleanVar()
    checkbutton = ttk.Checkbutton(text="Clicker ici quand c'est vrai",variable=vrai_ou_faux)
    checkbutton.pack()

def combobox():
    # creation d'un dropdown menu
    # utiliser le TKK aussi ici
    dropdown_option = tk.StringVar()

    my_dropdown = ttk.Combobox(parent_window, textvariable = dropdown_option,
                values = ["Dejeuner","Souper"])
    my_dropdown.pack()

def spinbox():
    # creation d'un input ou on peut changer la valeure avec key presses
    variable_text = tk.DoubleVar()
    # int-> 1,2,3
    # double (comme float) -> 1.3,1.5,1.9

    spin_box = tk.Spinbox(
        parent_window,
        from_ = 0.0,
        to = 5.0,
        increment = 0.5,
        textvariable = variable_text
    )
    spin_box_2 = tk.Spinbox(
        parent_window,
        from_ = 0,
        to = 5,
        increment = 1,
        textvariable = variable_text
    )
    spin_box.pack()
    spin_box_2.pack()

def scrollText():
    txt = tkst.ScrolledText(parent_window,width=50,height=50)
    txt.grid(column=0,row=100)

def progressBar():
    # la semaine prochaine
    print("progress bar")

def main():
    #C'est la fonction ou on va appeler toute les fonctions qu'on va mettre dans la fenetre
    #scrollText()
    canvas()
    user_inputs()
    radiobuttons()
    bouton_allo()
    bouton_exit()
    checkbutton()
    combobox()
    spinbox()
main()
parent_window.mainloop()


