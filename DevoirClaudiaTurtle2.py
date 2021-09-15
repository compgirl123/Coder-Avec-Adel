import turtle
import sys

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
    user_input = input("Choisi une couleur: 1.light blue 2.light green, 3.cyan 4.red 5.white 6.effacer le dessin ")
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
    elif user_input == "6":
        turtle.reset()
        turtle.done()
    elif user_input == "exit":
        exit_confirmation()
    else:
        print("Choisissez entre 1 à 5")
        user_choice()

def shape_choice():
        user_input = input("Choisi une forme: 1.carré 2.parallélogramme 3.carré avec parralélogramme ")
        if user_input == "1":
            user_shape = input("Quel type de carré voulez vous: 1.carré normal 2.double carré 3.triple carré ")
            # probleme
            if user_shape == "1":
                print("Bonjour")
                # probleme avec square
                square()
            elif user_shape == "2":
                doublesquare()
            elif user_shape == "3":
                triplesquare()
            else:
                print("choisissez entre 1 à 3")
                shape_choice()
        elif user_input == "2":
            # marche bien
            parallelogramme()
        elif user_input == "3":
            square()
            parallelogramme()
        elif user_input == "exit":
            exit_confirmation()
        else:
            print("Choisissez entre 1 à 3")
            shape_choice()

def shape_choice_2():
    user_input = input("Choisi une forme: 1.carré 2.parallélogramme 3.carré avec parralélogramme 4.Changer la couleur ")
    print(user_input)
    if user_input == "1":
        user_shape = input("Quel type de carré voulez vous: 1.carré normal 2.double carré 3.triple carré ")
        if user_shape == "1":
            square()
        elif user_shape == "2":
            doublesquare()
        elif user_shape == "3":
            triplesquare()
        else:
            print("choisissez entre 1 à 3")
            shape_choice()
    elif user_input == "2":
            parallelogramme()
    elif user_input == "3":
        square()
        print("bonjour")
        #parallelogramme()
    elif user_input == "4":
        user_choice()
        shape_choice_2()
    elif user_input == "exit":
        exit_confirmation()
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
        #regarde la fonction reset et done
        dessin.reset()
        turtle.done()
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
    shape_choice_2()
    
user_choice()
shape_choice()

while True:
    turtle.reset()
    main_function()

turtle.done()