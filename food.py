# to spawn food

from turtle import Turtle
import random as rd
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_len= 0.5 , stretch_wid= 0.5)
        self.penup()
        xcor = rd.randint(-13 , 13)
        ycor = rd.randint(-13 , 13)
        self.goto(xcor * 20 , ycor * 20 ) 
        self.speed("fastest")
    
    def refresh(self):
        xcor = rd.randint(-13 , 13)
        ycor = rd.randint(-13 , 13)
        self.goto(xcor * 20 , ycor * 20 )