from turtle import Turtle, Screen, penup

nit = Turtle()
scr = Screen()

def move_forward():
    nit.forward(10)
    
def move_backward():
    nit.backward(10)

def turn_left():
    nit.left(10)
    nit.forward(10)
    
def turn_right():
    nit.right(10)
    nit.forward(10)
    
def clear():
    nit.clear()
    nit.penup()
    nit.home()
    nit.pendown()
             
            

    
scr.listen()
scr.onkey(move_forward, "w")
scr.onkey(move_backward, "s")
scr.onkey(turn_left, "a")
scr.onkey(turn_right, "d")
scr.onkey(clear, "c")
scr.exitonclick()