from turtle import Turtle, Screen
import time
# Setting up the screen

s1 = Screen()
s1.setup(width=600 , height= 600)
s1.bgcolor("black")
s1.title("Snake")

# Making the snake body
body = []
for _ in range( 0 , 3):
    part = Turtle()
    part.shape("square")
    part.color("white")
    part.penup()
    part.goto( 0 - (_ * 20 ) , 0)
    body.append(part)

# Moving the snake body
s1.tracer(0)  # stop updating the screen
game_is_on = True
while game_is_on:           # start   stop  step
    for every_part in range(len(body) -1 , 0 , -1):
         new_x = body[every_part - 1].xcor() 
         new_y = body[every_part - 1].ycor()
         body[every_part] .goto(new_x,new_y)
    body[0].fd(20)
    time.sleep(0.1)
    s1.update() # calls all the updates from s1.tracer and will act at once






s1.exitonclick()
