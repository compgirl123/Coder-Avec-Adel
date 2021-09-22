
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

dessin = turtle.Turtle()

def square():
        dessin2 = turtle.Turtle()
        colors = ['lime green','tomato','pale violet red','steel blue']
        for i in range(4):
            dessin2.color(colors[i])
            dessin2.forward(90)
            dessin2.left(90)
        
def triangle():
    dessin.color("red")
    dessin.left(90)
    dessin.forward(90)
    dessin.right(90)
    
    
    for i in range(3):
        dessin.forward(90)
        dessin.left(120)

def porte():
    dessin.color("blue")
    dessin.right(90)
    dessin.forward(90)
    dessin.left(90)
    dessin.forward(30)
    dessin.left(90)
    for i in range(2):
        dessin.forward(45)
        dessin.right(90)
        dessin.forward(30)
        dessin.right(90)
    dessin.goto(90,0)
        
#def deplace_fleche():
    

square()
#deplace_fleche()
triangle()
porte()
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