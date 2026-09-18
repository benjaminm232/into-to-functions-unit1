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

""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90) 

def addSquares(iRange):
    length = 5
    for i in range(iRange):
        star(length)
        length += 5
        t.right(5)
addSquares(60) """

def star(x):
    for i in range(5):
        t.forward(150) 
        t.right(144) 

def addStar(iRange):
    length = 5
    for i in range(iRange):
        star(length)
        length += 5
        t.right(5)
addStar(60)

turtle.done()