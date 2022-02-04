from turtle import Turtle, Screen


PRERNA = Turtle() #assigning Turtle module to a var
PRERNA.shape("turtle") #changing shape
PRERNA.color("red") #chaning color
PRERNA.forward(10) #moving the turtle forward by 100
PRERNA.circle(100) #drawing the circle 

my_screen = Screen() #assigning screen module to var myscreen
print(my_screen.canvheight)
my_screen.title("Welcome to Turtle game night with Prerna")
my_screen.exitonclick() #exits the screen on click by user



