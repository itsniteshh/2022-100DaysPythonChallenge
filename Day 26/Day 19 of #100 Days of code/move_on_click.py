from turtle import Turtle, Screen


nit = Turtle()
scr = Screen()


def move_forward():
    nit.forward(10)


scr.listen()
scr.onkey(key="space", fun= move_forward)
scr.exitonclick() 