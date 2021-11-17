from tkinter import *

root = Tk()
root.geometry("550x150")
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
    
def nombre():
    sommation = 1
    valeur_input_box = int (entryNumber.get())
    for i in range(1, valeur_input_box+1):
        resultat = sommation - (sommation-1)
        sommation *= i
        taxe = (15*sommation)/100
        #resultat = Label(root, text=sommation)
        #resultat.place(x=200,y=50)
    label_resultat['text'] = "(avec taxe)Le résultat est " + str(sommation+taxe)
    label_resultat.place(x=200,y=50)

# creation des labels sur l'ecran
entrer_la_valeure = Label(root, text = "Entrer la valeur de l'integer n")
entrer_la_valeure.place(x=20,y=20)

entryNumber = Entry(root)
entryNumber.place(x = 200, y =20, width = 250)


# creation d'un label pour faire apparaitre le resultat
label_resultat = Label(root, text= "")
label_resultat.place(x = 200, y = 50)

# bouton pour la validation du resultat mathematique
bouton_validation = Button(root, text = "Validation" , command = nombre)
bouton_validation.place( x= 200, y= 90, width = 250)
root.mainloop()



