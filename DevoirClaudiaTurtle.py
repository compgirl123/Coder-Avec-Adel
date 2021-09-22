import turtle
import sys

extra = [" 6.effacer le dessin", " 7.changer la couleur "]
text = "Choisi une couleur: 1.light blue 2.light green, 3.cyan 4.red 5.white "
text_2 = "Choisi une forme: 1.carré 2.parallélogramme 3.carré avec parralélogramme "
screen = turtle.Screen()
couleurs = ['lightblue','lightgreen','cyan','red','white']
screen.bgcolor(couleurs[0])
dessin = turtle.Turtle() # definir un nouveau dessin dans tortue

def exit_confirmation():
    exit_confirmation = input("Êtes vous sûr vous voulez quitter? ")
    if exit_confirmation == "oui":
        print("Au revoir!")
        sys.exit()
    elif exit_confirmation == "non":
        user_choice()

def user_choice():
    user_input = input(text)
    if user_input == "1":
        screen.bgcolor(couleurs[0])
    elif user_input == "2":
        screen.bgcolor(couleurs[1])
    elif user_input == "3":
        screen.bgcolor(couleurs[2])
    elif user_input == "4":
        screen.bgcolor(couleurs[3])
    elif user_input == "5":
        screen.bgcolor(couleurs[4])
    elif user_input == "exit":
        exit_confirmation()
    else:
        print("Choisissez entre 1 à 5")
        user_choice()

def shape_choice():
        global text_2
        user_input = input(text_2)
        if user_input == "1":
            user_shape = input("Quel type de carré voulez vous: 1.carré normal 2.double carré 3.triple carré ")
            if user_shape == "1":
                dessin.reset()
                square()
            elif user_shape == "2":
                dessin.reset()
                doublesquare()
            elif user_shape == "3":
                dessin.reset()
                triplesquare()
            else:
                print("choisissez entre 1 à 3")
                shape_choice()
        elif user_input == "2":
            dessin.reset()
            parallelogramme()
        elif user_input == "3":
            dessin.reset()
            square()
            parallelogramme()
        elif user_input == "exit":
            exit_confirmation()
        elif user_input == "6":
            dessin.reset()
            shape_choice()
        elif user_input == "7":
            user_choice()
            shape_choice()
        else:
            print("Choisissez entre 1 à 3")
            shape_choice()
        
def parallelogramme():
        #dessin = turtle.Turtle() # definir un nouveau dessin dans tortue
        dessin.forward(90)
        dessin.left(45)

        dessin.forward(90)
        dessin.right(45)

        dessin.backward(90)
        dessin.left(45)
        dessin.backward(90)

def square():
        #turtle.done()
        dessin2 = turtle.Turtle()
        for i in range(4):
            dessin2.forward(90)
            dessin2.left(90)

def doublesquare():
        square()
        dessin2 = turtle.Turtle()
        for i in range(4):        
            dessin2.forward(150)
            dessin2.left(90)

def triplesquare():
        doublesquare()
        dessin2 = turtle.Turtle()
        for i in range(4):
            dessin2.forward(210)
            dessin2.left(90)

def main_function():
    global text_2
    shape_choice()
    text_2 = "Choisi une forme: 1.carré 2.parallélogramme 3.carré avec parralélogramme" + extra[0] + extra[1]

    
user_choice()
while True:
    main_function()
    

turtle.done()