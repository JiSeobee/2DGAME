import turtle as t
from random import *

def drunken_move():
    t.setheading(randint(0,360))
    t.forward(randint(50,300))
    t.stamp()

t.shape('turtle')

t.onkey(drunken_move, ' ')
t.listen()
