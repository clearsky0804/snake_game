from turtle import Turtle
INITIAL_COORDINATES = [ (0, 0 ) , (-20, 0 ) , (-40 , 0) ]
FIXED_DISTANCE = 20
class Snake:  # attributes of snake are body parts
    def __init__(self):
        self.body = []
        for _ in range( 0 , 3):
            part = Turtle()
            part.shape("square")
            part.color("white")
            part.penup()
            part.goto(INITIAL_COORDINATES[_])
            self.body.append(part)
        self.head = self.body[0]
        self.body_length = len(self.body) 
        self.tail = self.body[self.body_length - 1]

    def const_movement(self):
        for every_part in range(len(self.body) - 1, 0 ,-1):
            new_x = self.body[every_part - 1].xcor() 
            new_y = self.body[every_part - 1].ycor()
            self.body[every_part] .goto(new_x,new_y)
        self.head.forward(FIXED_DISTANCE)
    
    def extension(self):
        new_part = Turtle()
        new_part.shape("square")
        new_part.color("white")
        new_part.penup()
        xcoor = self.tail.xcor()
        ycoor = self.tail.ycor()
        if self.tail.heading() == 0:
            new_part.goto(xcoor  , ycoor + 20)
        if self.tail.heading() == 180:
            new_part.goto(xcoor  , ycoor - 20)
        if self.tail.heading() ==90:
            new_part.goto(xcoor +20  , ycoor )
        if self.tail.heading() == 270:
            new_part.goto(xcoor - 20 , ycoor )
        self.body.append(new_part)

    # defining moment
    def up(self):
        if self.head.heading() != 180:
            self.head.seth(0)
            
    def left(self):
        if self.head.heading() != 90:
            self.head.seth(270)
            
    def right(self):
        if self.head.heading() != 270:
            self.head.seth(90)
            
    def down(self):
        if self.head.heading() !=0:
            self.head.seth(180)
      
