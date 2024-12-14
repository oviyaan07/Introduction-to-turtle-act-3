import turtle

screen=turtle.Screen()
screen.bgcolor("black")

t=turtle.Turtle()
t.color("white")

size=0
while True:
    for i in range(4):
        t.forward(size+1)
        t.left(90)
        size=size-5
    size=size+1