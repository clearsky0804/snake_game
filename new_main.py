from turtle import Screen , Turtle
import time
from snake import Snake
from food import Food
from scorecard import Scorecard
import math

s1 = Screen()
s1.setup(width=600 , height= 600)
s1.bgcolor("black")
s1.title("Snake")
s1.mode("logo")

snake = Snake()
food = Food()
scorecard = Scorecard()


boundary = Turtle()
boundary.shape("square")
boundary.pencolor("white" )
boundary.fillcolor("")
boundary.shapesize(29, 29 , 3)

s1.tracer(0)
s1.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s1.onkey(snake.up , "Up")
    s1.onkey(snake.down , "Down")
    s1.onkey(snake.left , "Left")
    s1.onkey(snake.right , "Right")
    snake.const_movement()
    if snake.head.distance(food) < 15:
        scorecard.update_score()
        food.refresh()
        snake.extension()
    if snake.head.xcor() >= 280 or snake.head.ycor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        scorecard.gameover()
        game_is_on = False 
    for segment in snake.body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scorecard.gameover()
    s1.update()
    


s1.exitonclick()