from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("Blue")
"""
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
"""

for movement in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)




my_screen = Screen()
my_screen.exitonclick()