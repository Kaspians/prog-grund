#!/bin/python3
#
# 2 paddor

import turtle
import random

turtle.Screen().bgcolor("gray")
turtle.Screen().delay(0)

y = int(turtle.window_height())
x = int(turtle.window_width())
print(f"x{x}\ny{y}\n")
print(f"div2\nx/2 = {x//2}\ny/2 = {y//2}\n")

foobar = turtle.Turtle()
barfoo = turtle.Turtle()


def maketurtle(name, color, x, y):
    name.shape("turtle")
    name.pencolor(color)
    name.penup()
    name.goto(x, y)
    name.pendown()


# ruta 1000,800
maketurtle(foobar, "green", -x / 6, -y / 4)
maketurtle(barfoo, "red", -x / 6, y / 4)


def random_step(turtles):
    turtles.forward(random.randint(5, 15))
    rikt = random.randint(1, 2)
    if rikt == 1:
        turtles.left(45)
    else:
        turtles.right(45)


def border(turt):
    y2 = int(turtle.window_height() / 2)
    x2 = int(turtle.window_width() / 2)
    turty = turt.ycor()
    turtx = turt.xcor()
    if turtx >= int(x2) or turtx <= -int(x2):
        print(f"turtx = {turtx}")
        turt.goto(-(turtx), -(turty))
        # ↓ troligen onödigt
        if turtx > 0:
            turt.goto(turtx - 100, turty)
        else:
            turt.goto(turtx + 100, turty)
    if turty >= int(y2) or turty <= -int(y2):
        print(f"turty = {turty}")
        turt.goto(-(turtx), -(turty))
        # ↓ troligen onödigt
        if turty > 0:
            turt.goto(turtx, turty - 100)
        else:
            turt.goto(turtx, turty + 100)


while foobar.distance(barfoo) > 100:
    random_step(foobar)
    border(foobar)
    random_step(barfoo)
    border(barfoo)

print("Nära!")
turtle.mainloop()
