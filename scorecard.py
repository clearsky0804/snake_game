ALIGN = "center"
FONT = ("Arial" , 24," normal")



from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0 , 300)
        self.write(f"Score:{self.score}", align = ALIGN , font = FONT)
        self.hideturtle()
    def increase_score(self):
        self.score += 1
    def update_score(self):
        self.reset()
        self.increase_score()
        self.penup()
        self.color("white")
        self.goto(0 , 300)
        self.write(f"Score:{self.score}", align =ALIGN , font = FONT)
        self.hideturtle()

    def gameover(self):
        self.reset()
        self.goto(0 , 0)
        self.penup()
        self.color("white")
        self.write(f"GAME OVER:Your score is {self.score}.", align =ALIGN , font = FONT)
        self.hideturtle()