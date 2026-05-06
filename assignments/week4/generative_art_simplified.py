from turtle import *
import random
width = 600
height = 600
setup(width, height)
tracer(0, 0)
rand_turn = random.randint(0, 360)
old_coord = (0, 0)
amount = 30
penup()
color("black")
goto(-72,70)
pendown()
for i in range(5000):
    rand_turn = random.randint(0, 360)
    right(rand_turn)
    penup()
    old_coord = pos()
    forward(amount)
    if xcor() > 200 or xcor() < -200:
        goto(*old_coord)
    elif ycor() > 200 or ycor() < -200:
        goto(*old_coord)
    elif distance(0, 0) < 90:
        goto(*old_coord)
    else:
        goto(*old_coord)
        pendown()
        forward(amount)
hideturtle()
update()
done()
