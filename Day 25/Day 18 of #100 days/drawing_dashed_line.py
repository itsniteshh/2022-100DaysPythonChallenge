from turtle import Turtle, Screen

tur = Turtle()
tur.shape("turtle")
tur.color("red")
tur.speed(2)

for move in range(5):
    tur.penup()
    tur.forward(20)
    tur.pendown()
    tur.forward(20)




sc = Screen()
sc.exitonclick()