import time
from turtle import Turtle,Screen
class Pedal:
    def __init__(self,coordinates,screen):
        self.blocks=[]
        self.screen=screen
        self.coordinates=coordinates
        for i in range(0,3):
            newblock=Turtle(shape="square")
            newblock.color("white")
            newblock.pu()
            newblock.setheading(90)
            newblock.goto(self.coordinates[i])
            self.blocks.append(newblock)
            self.screen.update()
    def goup(self):
        self.blocks[2].goto(self.blocks[1].position())
        self.blocks[1].goto(self.blocks[0].position())
        self.blocks[0].forward(20)
        self.screen.update()
    def godown(self):
        self.blocks[0].goto(self.blocks[1].position())
        self.blocks[1].goto(self.blocks[2].position())
        self.blocks[2].setheading(270)
        self.blocks[2].forward(20)
        self.screen.update()

