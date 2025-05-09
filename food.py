# to spawn food

from turtle import Turtle
import random as rd
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_len= 0.5 , stretch_wid= 0.5)
        xcor = rd.randint(-13 , 13)
        ycor = rd.randint(-13 , 13)
        self.goto(xcor * 20 + 5, ycor * 20 + 5) 
        self.speed("fastest")
    
    def refresh(self):
        random_x = rd.randint(-280, 280)
        random_y = rd.randint(-280, 280)
        self.goto(random_x,random_y)