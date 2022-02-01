from turtle import *
import random

col = ["red", "blue", "black", "green", "yellow", "grey", "pink"]

tur = Turtle()
tur.shape("arrow")
tur.circle(100)


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tur.forward(100)
        tur.right(angle)
        tur.color(random.choice(col))
        

for shapess in range(3, 11):
    draw_shapes(shapess)



scr = Screen()
scr.exitonclick()

