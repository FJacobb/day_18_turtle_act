import random
from turtle import *
import colorgram
def dot():
    festus.pendown()
    festus.forward(0)
    festus.penup()
    festus.forward(20)
    festus.pendown()
def move(y):
    festus.penup()
    festus.goto(x=-310, y=y)
rgb =[]
color = colorgram.extract("image.jpg",30)
for x in color:
    rgb.append(x.rgb)
festus = Turtle()
festus.pensize(10)
festus.penup()
festus.goto(x=-310, y=-270)
festus.speed(10)
colormode(255)
y=-270
while y <= 270:

    move(y)
    for s in range(31):
        festus.color(random.choice(rgb))
        dot()
    y+=20

screen =Screen()

screen.exitonclick()