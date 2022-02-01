
import random
from turtle import *

colors = ["Red", "orange", "grey", "pink", "white", "black", "green", "violet", "blue"]
directions = [0, 90, 180, 270]

prerna = Turtle()
prerna.shape("turtle")
prerna.color(random.choice(colors))




for i in range(100):
    prerna.forward(30)
    prerna.setheading(random.choice(directions))
    prerna.color(random.choice(colors))


scr = Screen()
scr.exitonclick()