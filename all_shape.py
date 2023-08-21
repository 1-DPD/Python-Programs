import random
import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
color = ['red', 'yellow', 'orange', 'green']


def shape_side(side):
    angle = 360 / side
    for i in range(side):
        t.forward(50)
        t.left(angle)


for j in range(3, 16):
    t.pencolor(color[j % 4])
    shape_side(j)


