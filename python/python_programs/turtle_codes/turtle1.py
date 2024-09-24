from turtle import *

pencil = Turtle()

colors = ["red", "purple", "orange", "lime green", "yellow", "blue"]


for i in range(6):
    pencil.pencolor(colors[i])
    pencil.width(5)
    pencil.fd(300)
    pencil.rt(60)

