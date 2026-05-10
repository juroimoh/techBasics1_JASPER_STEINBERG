# import
from turtle import *
import random

# setup
width = 800
height = 800
setup(width, height)

tracer(1000, 1) # Very fast speed.
# tracer(0, 0) # Instant speed.

rand_turn = random.randint(0, 360)
old_coord = (0, 0)
amount = 30 # Length of the lines (currently the length is randomized between 10 and 60).

outline = 0 # Change to 1 if you want a box around the main area (if you want that for some reason).
extra = 0 # Change to 1 if you want to see my first art idea (a 3d cone) before I had this idea.
nested = 1 # This was added later, after realizing we needed to add a nested loop. This adds dots around the screen!

colors = ["#FF1717","#D3151F","#C41333","#A01037","#870D52"]

# art
penup()
color("black")
goto(-72,70) # Starting point, in a location that feels random.
pendown()

for i in range(5000):
    rand_turn = random.randint(0, 360)
    amount = random.randint(10,60) # Random line length, delete for equal lengths (in line 17).
    right(rand_turn)
    penup()
    old_coord = pos()
    forward(amount)
    if xcor() > 200 or xcor() < -200:
        goto(*old_coord) # Used Gemini to solve this issue, reading old_coord as two values (using an asterix).
    elif ycor() > 200 or ycor() < -200:
        goto(*old_coord)
    elif distance(0, 0) < 90:
        goto(*old_coord)
    else:
        goto(*old_coord)
        pendown()
        forward(amount)
        color(random.choice(colors)) # Random colors, delete to make all lines black.

rand_coord_x = 0
rand_coord_y = 0

if nested == 1:
    for i in range(8): # This whole part could probably somehow be cleaned up a bit.
        penup()
        rand_coord_x = random.randint(-350, 350)
        rand_coord_y = random.randint(-350, 350)
        goto(rand_coord_x, rand_coord_y)
        while distance(0, 0) < 300:
            rand_coord_x = random.randint(-350, 350)
            rand_coord_y = random.randint(-350, 350)
            goto(rand_coord_x, rand_coord_y)
        goto(rand_coord_x, rand_coord_y)
        pendown()
        old_coord = pos()
        for e in range(200):
            rand_turn = random.randint(0, 360)
            amount = random.randint(10, 40)
            right(rand_turn)
            penup()
            old_coord = pos()
            forward(amount)
            if distance(rand_coord_x, rand_coord_y) > 30:
                goto(*old_coord)
            else:
                goto(*old_coord)
                pendown()
                forward(amount)
                color(random.choice(colors))

if outline == 1:
    penup()
    goto(-210, 210)
    pendown()
    color("#000000")
    setheading(0)
    for i in range(4):
        forward(420)
        right(90)
    penup()
    goto(0, -80)
    pendown()
    setheading(0)
    circle(80, 360)

if extra == 1:
    penup()
    goto(0, -80)
    setheading(0)
    hex = 0x100000 # Gemini helped with converting the hex into a hex string using '0x'
    rad = 80
    prevy = 0
    for y in range(200):
        shade = f"#{hex:06x}" # Gemini helped with converting the shade into using hex string up to 6 digits to prevent overflow.
        pendown()
        begin_fill()
        fillcolor(shade)
        color(shade)
        circle(rad, 360)
        end_fill()
        penup()
        prevy += 1
        goto(0, -80 + prevy * 4)
        setheading(0)
        rad -= 1.2
        if rad < 0:
            rad = 0
        hex += 3

# end
hideturtle() # Used Gemini to find this setting.
update()
done()

# The idea for this project I managed to execute exactly as I wanted, which I'm really happy about.
# I'm really surprised I've been able to fit everything into such few lines, especially with the extra additions (random colors, line lengths, etc.).
# Concerning the actual art, I am a much bigger fan of the simpler generative_art_simplified.py art, without the additions above (which was also the original idea).
# The variables 'outline' and 'extra' can be toggled to view the other ideas I've tried, but I've kept them off by default to avoid clutter.

# When condensing this project to my original plan, the code is only 32 lines (see generative_art_simplified.py).
# I find the colors and extra features unnecessary, but they show what I've tried and managed to accomplish.

# This project was inspired by the generative cube art we looked at in class. I wanted to make something similar, where the art is actually computer generated and not just drawing instructions copied by a computer.
# ദ്ദി◝ ⩊ ◜.ᐟ
