# import
from turtle import *
import random

# setup
width = 600
height = 600

setup(width, height)

tracer(1000, 1) # Very fast speed.
# tracer(0, 0) # Instant speed.

rand_turn = random.randint(0, 360)
old_coord = (0, 0)
amount = 30 # Length of the lines (currently the length is randomized between 10 and 60).

outline = 0 # Change to 1 if you want a box around the area (I have it off because I think it's ugly).
extra = 0 # Change to 1 if you want to see my first art idea (a 3d cone) before I had this idea.

colors = ["#FF1717","#D3151F","#C41333","#A01037","#870D52"]

# art
penup()
color("black")
goto(-72,70)
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

# The actual code for the main project is roughly ~30 lines, which is really cool (if you remove the random colors, line lengths, etc.).
# Everything extra I don't like. I would prefer having the lines all be black, the same length, and nothing extra.
# Everything else is added to show what I've discovered and tried, NOT what I find aesthetic.
# ദ്ദി◝ ⩊ ◜.ᐟ
