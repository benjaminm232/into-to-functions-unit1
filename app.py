import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(100)

""" def rectangle(x):
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
rectangle(200) """

def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)


def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length)
        length = length * 2
        t.right(5)
doubleSquares(100)

turtle.done()