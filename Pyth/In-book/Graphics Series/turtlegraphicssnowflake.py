from turtle import*
import random

t = Turtle()
t.hideturtle()
t.shape("turtle")
t.speed(10)
t.pensize(6)
Screen().bgcolor("turquoise")
colours = ["blue", "purple", "cyan", "white", "yellow", "green", "orange"]
def vshape(size):
    t.right(25)
    t.forward(size)
    t.backward(size)
    t.left(50)
    t.forward(size)
    t.backward(size)
    t.right(25)
def snowflakeArm(size):
    for x in range(0,4):
        t.forward(size)
        vshape(size)
    t.backward(size * 4)
def snowflake(size):
    for x in range(0,6):
        t.color(random.choice(colours))
        snowflakeArm(size)
        t.right(60)
for i in range(0,10):
    size = random.randint(5,30)
    x = random.randint(-400,400)          
    y = random.randint(-400,400)
    t.penup()
    t.goto(x,y)
    t.pendown()
    snowflake(size)          