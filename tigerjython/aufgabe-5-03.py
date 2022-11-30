from gturtle import *

def vieleck(n,seite):
    repeat n:
        forward(seite)
        right(360/n)
    forward(seite)

makeTurtle()
hideTurtle()

seite=40
repeat 6:
    vieleck(4,seite)
    left(360/6)
right(90)
forward(seite)
left(90)

repeat 6:
    vieleck(6,seite)
    left(360/12)
    vieleck(4,seite)
    left(360/12)
