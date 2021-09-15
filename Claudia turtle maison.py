
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

def square():
        dessin2 = turtle.Turtle()
        colors = ['lime green','tomato','pale violet red','steel blue']
        for i in range(4):
            dessin2.color(colors[i])
            dessin2.forward(90)
            dessin2.left(90)
        
square()
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