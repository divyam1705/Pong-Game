from turtle import Turtle,Screen
s2=Screen()
s2.tracer(0)
s2.bgcolor("black")
class Score(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0,280)
        self.score1=0
        self.score2=0
        self.write(arg=f"{self.score1}      {self.score2}",font=('Arial',20,"normal"),align="center")
        self.screen=screen
        self.screen.update()
        self.setmode()
    def updatescores(self):
        self.clear()
        self.write(arg=f"{self.score1}      {self.score2}",font = ('Arial', 20, "normal"), align = "center")
        self.screen.update()
    def setmode(self):
        self.setheading(270)
        while self.position()[1] >-280:
            self.pd()
            self.forward(10)
            self.pu()
            self.forward(10)
        self.goto(0, 280)
        self.screen.update()
    def gameover(self):
        self.goto(0,0)
        self.write(arg=f"score1={self.score1} score2={self.score2}", font=('Arial', 20, "normal"), align="center")
        self.goto(0,-50)
        self.color("red")
        self.write(arg="Game Over", font=('Arial', 20, "normal"), align="center")

    def boundary(self):
        self.goto(-300,300)
        self.pd()
        self.setheading(270)
        self.forward(600)
        self.setheading(0)
        self.forward(600)
        self.setheading(90)
        self.fd(600)
        self.setheading(180)
        self.fd(600)
        self.pu()
        self.goto(0,-280)
