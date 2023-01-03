import time
from turtle import Turtle,Screen
from pedal import Pedal
from pongball import PongBall
from scores import Score
s1=Screen()
s1.tracer(0)
s1.bgcolor("black")
s1.screensize(600,600)
s1.listen()
p1=PongBall(s1)
pedal1=Pedal([(-280,20),(-280,0),(-280,-20)],s1)
pedal2=Pedal([(280,20),(280,0),(280,-20)],s1)
scoreboard1=Score(s1)
s1.onkey(pedal2.goup,"Up")
s1.onkey(pedal2.godown,"Down")
s1.onkey(pedal1.goup,"w")
s1.onkey(pedal1.godown,"s")
game_on=True
x=pedal1.blocks
y=pedal2.blocks

while game_on:
    scoreboard1.boundary()
    for i in x:
        if i.distance(p1)<15:
            p1.reflect()
            scoreboard1.score1+=1
            scoreboard1.updatescores()
    for i in y:
        if i.distance(p1)<15:
            p1.reflect()
            scoreboard1.score2+=1
            scoreboard1.updatescores()
    if p1.position()[1] >280 or p1.position()[1] <-280 :
        p1.hitwall()
    if p1.position()[0] >300 or p1.position()[0] <-300:
        
        scoreboard1.gameover()
        game_on=False

    p1.move()










s1.exitonclick()
