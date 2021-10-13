
'''# importing package
import turtle
 
# use forward by 50 (default = black)
turtle.forward(50)
 
# change the color of turtle
turtle.color("red")
 
# use forward by 50 (color = red)
turtle.forward(50)

turtle.done()'''

import turtle
import sys

print("Dimensions de l'ecran", turtle.screensize())
dessin = turtle.Turtle()
colors = ["red", "blue", "green", "yellow", "orange", "black"]

def exit_confirmation():
    exit_choice = input("Êtes vous sûr que vous voulez quitter? ")
    if exit_choice == "oui":
        sys.exit()
    elif exit_choice == "non":
        color_choice()

def color_choice():
    user_input = input("Quel couleur veut-tu? 1.rouge 2.bleu 3.vert 4.jaune 5.orange 6.noir ")
    if user_input == "1":
        dessin.color(colors[0])
    elif user_input == "2":
        dessin.color(colors[1])
    elif user_input == "3":
        dessin.color(colors[2])
    elif user_input == "4":
        dessin.color(colors[3])
    elif user_input == "5":
        dessin.color(colors[4])
    elif user_input == "6":
        dessin.color(colors[5])
    elif user_input == "exit":
        exit_confirmation()
    else:
        print("choisi un nombre entre 1 à 6")
        color_choice()

def maison():
    def square():
        #dessin.clear()
        #dessin.goto(0, 0)
        #colors = ['lime green','tomato','pale violet red','steel blue']
        for i in range(4):
            #dessin2.color(colors[i])
            dessin.forward(90)
            dessin.left(90)

    def square_2():
        dessin.penup()
        dessin.clear()
        dessin.goto(0, 0)
        dessin.right(90)
        dessin.pendown()
        #colors = ['lime green','tomato','pale violet red','steel blue']
        for i in range(4):
            #dessin2.color(colors[i])
            dessin.forward(90)
            dessin.left(90)
        
    def triangle():
        #dessin.color("red")
        dessin.left(90)
        dessin.forward(90)
        dessin.right(90)
      
        for i in range(3):
            dessin.forward(90)
            dessin.left(120)

    def porte():
        #dessin.color("blue")
        dessin.right(90)
        dessin.forward(90)
        dessin.left(90)
        dessin.forward(30)
        dessin.left(90)
        for i in range(4):
            dessin.forward(45)
            dessin.right(90)
            dessin.forward(30)
            dessin.right(90)

        
    square()
    triangle()
    porte()
    #dessin.forward(90)

def number_choice():
    user_input = input("Combien de maison voulez vous? 1, 2, 3, 4 ")
    if user_input == "1":
        dessin.penup()
        dessin.goto(-290, 0)
        dessin.pendown()
        maison()
    elif user_input == "2":
        dessin.penup()
        dessin.goto(-290, 0)
        dessin.pendown()
        maison()
        dessin.penup()
        dessin.right(90)
        dessin.forward(90)
        dessin.goto(-140, 0)
        dessin.pendown()
        maison()
    elif user_input == "3":
        dessin.penup()
        dessin.goto(-290, 0)
        dessin.pendown()
        maison()
        dessin.penup()
        dessin.right(90)
        dessin.forward(90)
        dessin.goto(-140, 0)
        dessin.pendown()
        maison()
        dessin.penup()
        dessin.goto(10,0)
        dessin.pendown()
        dessin.right(90)
        maison()
    elif user_input == "4":
        dessin.penup()
        dessin.goto(-290, 0)
        dessin.pendown()
        maison()
        dessin.penup()
        dessin.right(90)
        dessin.forward(90)
        dessin.goto(-140, 0)
        dessin.pendown()
        maison()
        dessin.penup()
        dessin.goto(10,0)
        dessin.pendown()
        dessin.right(90)
        maison()
        dessin.penup()
        dessin.goto(160,0)
        dessin.pendown()
        dessin.right(90)
        maison()
        dessin.goto(250,0)
    else:
        print("Choisi un nombre entre 1 à 3")
        number_choice()

def flocon_neige():
    dessin.color("cyan")
    dessin.penup()
    dessin.goto(-290, 160)
    dessin.right(90)
    dessin.pendown()
    for i in range(6):
        for i in range(6):
            dessin.forward(13)
            dessin.left(60)
        dessin.left(60)
        dessin.forward(13)
        dessin.right(120)
        dessin.forward(13)
        dessin.left(120)
        dessin.forward(13)
        dessin.left(120)
        dessin.forward(13)
        dessin.right(120)
        dessin.forward(13)
        dessin.left(120)
        dessin.forward(13)
        dessin.left(120)
        dessin.forward(13)
        dessin.right(120)
        dessin.forward(13)
        dessin.left(120)
        dessin.forward(13)
        dessin.penup()
        dessin.left(60)
        dessin.forward(150)
        dessin.right(90)
        dessin.forward(45)
        dessin.pendown()
        for i in range(6):
            dessin.forward(13)
            dessin.left(60)
        dessin.left(60)
        dessin.forward(13)
        dessin.right(120)
        dessin.forward(13)
        dessin.left(120)
        dessin.forward(13)
        dessin.left(120)
        dessin.forward(13)
        dessin.right(120)
        dessin.forward(13)
        dessin.left(120)
        dessin.forward(13)
        dessin.left(120)
        dessin.forward(13)
        dessin.right(120)
        dessin.forward(13)
        dessin.left(120)
        dessin.forward(13)
        dessin.penup()
        dessin.left(60)
        dessin.forward(150)
        dessin.left(90)
        dessin.forward(45)
        dessin.pendown()
        dessin.left(60)
    
def bonhome_neige():
    dessin.penup()
    dessin.left(90)
    dessin.goto(-100, -75)
    dessin.pendown()
    for i in range(6):
        dessin.forward(15)
        dessin.left(60)
    dessin.left(60)
    dessin.forward(15)
    dessin.right(120)
    dessin.forward(15)
    dessin.left(120)
    dessin.forward(15)
    dessin.left(120)
    dessin.forward(15)
    dessin.right(120)
    dessin.forward(15)
    dessin.left(120)
    dessin.forward(15)
    dessin.left(120)
    dessin.forward(15)
    dessin.right(120)
    dessin.forward(15)
    dessin.left(120)
    dessin.forward(15)
    dessin.right(60)
    for i in range(6):
        dessin.forward(30)
        dessin.left(60)
    dessin.left(60)
    dessin.forward(30)
    dessin.right(120)
    dessin.forward(30)
    dessin.left(120)
    dessin.forward(30)
    dessin.left(120)
    dessin.forward(30)
    dessin.right(120)
    dessin.forward(30)
    dessin.left(120)
    dessin.forward(30)
    dessin.left(120)
    dessin.forward(30)
    dessin.right(120)
    dessin.forward(30)
    dessin.left(120)
    dessin.forward(30)
    dessin.left(60)
    dessin.penup()
    dessin.forward(30)
    dessin.left(60)
    dessin.forward(30)
    dessin.left(60)
    #dessin.forward(60)
    dessin.right(120)
    dessin.pendown()
    for i in range(6):
        dessin.forward(45)
        dessin.left(60)
    dessin.left(60)
    dessin.forward(45)
    dessin.right(120)
    dessin.forward(45)
    dessin.left(120)
    dessin.forward(45)
    dessin.left(120)
    dessin.forward(45)
    dessin.right(120)
    dessin.forward(45)
    dessin.left(120)
    dessin.forward(45)
    dessin.left(120)
    dessin.forward(45)
    dessin.right(120)
    dessin.forward(45)
    dessin.left(120)
    dessin.forward(45)

def bonhome_choice():
    user_input = input("Voulez vous un bonhome de neige? 1.oui 2.non ")
    if user_input == "1":
        bonhome_neige()
    elif user_input == "2":
        pass
    else:
        print("choisi 1 ou 2")
        bonhome_choice()

def flocon_choice():
    user_input = input("Voulez vous des flocons? 1.oui 2.non ")
    if user_input == "1":
        flocon_neige()
    elif user_input == "2":
        pass
    else:
        print("choisi 1 ou 2")
        flocon_choice()

def arbre():
    dessin.penup()
    dessin.goto(100, -75)
    dessin.pendown()
    def hexagon():
        dessin.color("green")
        for i in range(6):
            dessin.forward(45)
            dessin.left(60)
        dessin.left(60)
        dessin.forward(45)
        dessin.right(120)
        dessin.forward(45)
        dessin.left(120)
        dessin.forward(45)
        dessin.left(120)
        dessin.forward(45)
        dessin.right(120)
        dessin.forward(45)
        dessin.left(120)
        dessin.forward(45)
        dessin.left(120)
        dessin.forward(45)
        dessin.right(120)
        dessin.forward(45)
        dessin.left(120)
        dessin.forward(45)
    def tronc():
        dessin.color("brown")
        dessin.penup()
        dessin.left(60)
        dessin.forward(22.5)
        dessin.pendown()
        dessin.right(90)
        dessin.forward(120)
    hexagon()
    tronc()

def arbre_choice():
    user_input = input("Voulez vous un arbre? 1.oui 2.non ")
    if user_input == "1":
        arbre()
    elif user_input == "2":
        pass
    else:
        print("choisi un ou deux")
        arbre_choice()


        
#def deplace_fleche():
#dessin.hideturtle()
dessin.speed(10)
color_choice()
number_choice()
flocon_choice()
arbre_choice()
bonhome_choice()
#dessin.right(90)
#arbre()
#flocon_neige()
#bonhome_neige()





#while True: 
#    color_choice()
 #   number_choice
  #  square_2()
#deplace_fleche()
 #   triangle()
  #  porte()

turtle.done()

'''from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()'''