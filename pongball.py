from turtle import Turtle,Screen
import time
class PongBall(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5,0.5)
        #self.pu()
        self.setheading(60)
        self.screen=screen
    def reflect(self):

        if self.heading()>180 :
            if self.position()[0]>0:
                self.setheading(self.heading()-60)
            else:
                self.setheading(self.heading() + 60)

            self.move()
            time.sleep(0.1)
            self.screen.update()
        elif self.heading()<180 and self.heading()>0:
            self.setheading(180-self.heading())
            self.move()
            time.sleep(0.1)
            self.screen.update()


        else:
            self.setheading(self.heading() + 180)
            self.move()
            time.sleep(0.1)
            self.screen.update()
    def move(self):
        self.forward(10)
        time.sleep(0.1)
        self.screen.update()
    def hitwall(self):
        self.setheading(360-self.heading())
        self.move()
        time.sleep(0.1)
        self.screen.update()

