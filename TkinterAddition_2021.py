from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk


root = Tk()
root.geometry("730x280")

# geometry et canvas -> similaires, ils sont 2 differentes
# representations de la meme chose (l'ecran).

def prendre_input():
    ''' prendre valeure de input box et sauvegarde dans 
    une variable '''
    # commence a 1 et arrete a le numero dans valeur_input_box
    # 5-> 1+2+3+4+5
    #label_resultat['text'] = nombre
    print("faire apres")
    valeur_input_box = int (entryNumber.get())
    valeur_input_box = int (entryNumber2.get())
    valeur_input_box = int (entryNumber3.get())
    valeur_input_box = int (entryNumber4.get())

def nombre():
    sommation = 1
    valeur_input_box = int (entryNumber.get())
    for i in range(1, valeur_input_box+1):
        resultat = sommation - (sommation-1)
        sommation *= i
        #resultat = Label(root, text=sommation)
        #resultat.place(x=200,y=50)
    label_resultat['text'] = "Le résultat de factorial est " + str(sommation)
    label_resultat.place(x=0,y=160)    

    # bouton pour la validation du resultat mathematique
bouton_validation3 = Button(root, text = "Validation pour factorial", fg = 'orange', command = nombre)
bouton_validation3.place(x= 0, y= 140, width = 180)

def nombre_taxe():
    valeur_input_box = int (entryNumber2.get())
    taxe = (15*valeur_input_box)/100
    label_resultat2["text"] = "Le résultat taxe est " + str(taxe)
    label_resultat2.place(x=0,y=180)


def nombre_deux():
    sommation = 1
    valeur_input_box = int (entryNumber3.get())
    for i in range(1, valeur_input_box+1):
        resultat = sommation - (sommation-1)
        sommation *= i
        taxe = (15*sommation)/100
    label_resultat3["text"] = "Le résultat des deux sont " + str(sommation+taxe)
    label_resultat3.place(x=0,y=200)

def nombre_prix():
    valeur_input_box = int (entryNumber4.get())
    taxe = (15*valeur_input_box)/100
    label_resultat4["text"] = "Le résultat du prix est " + str(valeur_input_box+taxe)
    label_resultat4.place(x=0,y=220)
    def information_taxe():
        taxe_total = Label(root, text = "Le montant du taxe est" + str((15*valeur_input_box)/100))
        taxe_total.place(x= 540, y= 40)
    taxe_info = Button(root, text= "Informations sur les taxes", fg = "blue", command = information_taxe)
    taxe_info.place(x= 540, y= 20)  

# creation des labels sur l'ecran
entrer_la_valeure = Label(root, fg = "red", bg = "pink", text = "Entrer la valeur de l'integer(Pour factorial) ")
entrer_la_valeure.place(x=20,y=20)

entryNumber = Entry(root)
entryNumber.place(x = 300, y =20, width = 250)

# creation d'un label pour faire apparaitre le resultat
label_resultat = Label(root, text= "")
label_resultat.place(x = 200, y = 50)
label_resultat2 = Label(root, text= "")
label_resultat2.place(x = 200, y = 50)
label_resultat3 = Label(root, text= "")
label_resultat3.place(x = 200, y = 50)
label_resultat4 = Label(root, text= "")
label_resultat4.place(x = 200, y = 50)

# bouton pour la validation du resultat mathematique
bouton_validation = Button(root, fg = "orange", text = "Validation pour les deux" , command = nombre_deux)
bouton_validation.place( x= 360, y= 140, width = 180)

# bouton pour la validation du resultat mathematique
bouton_validation2 = Button(root, fg = "orange", text = "Validation pour taxe" , command = nombre_taxe)
bouton_validation2.place( x= 180, y= 140, width = 180)



# bouton pour la validation du resultat mathematique
bouton_validation4 = Button(root, fg = "orange", text = "Validation pour prix" , command = nombre_prix)
bouton_validation4.place(x= 540, y= 140, width = 180)

# creation des labels sur l'ecran
entrer_la_valeure2 = Label(root, fg = "orange", bg = "pink", text = "Entrer la valeur de l'integer(Pour taxe) ")
entrer_la_valeure2.place(x=20,y=50)

entryNumber2 = Entry(root)
entryNumber2.place(x = 300, y =50, width = 250)

# creation des labels sur l'ecran
entrer_la_valeure3 = Label(root, fg = "red", bg = "pink", text = "Entrer la valeur de l'integer(Pour les deux) ")
entrer_la_valeure3.place(x=20,y=80)

entryNumber3 = Entry(root)
entryNumber3.place(x = 300, y =80, width = 250)

entrer_la_valeure4 = Label(root, fg = "orange", bg = "pink", text = "Entrer la valeur de l'integer(Pour prix) ")
entrer_la_valeure4.place(x=20,y=110)

entryNumber4 = Entry(root)
entryNumber4.place(x = 300, y =110, width = 250)

def progress_bar():
    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar",background='blue')
    bar = Progressbar(root, length=220,style='black.Horizontal.TProgressbar')
    bar['value'] = 35
    bar.grid(column=0,row=6)
    bar.place(x= 270, y= 180)

progress_bar()

root.mainloop()

