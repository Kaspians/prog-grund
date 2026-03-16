#!/bin/python3
#
# randomwalk.py

# 3
#
import turtle
import random
foobar = turtle.Turtle()
for i in range(100):
    rikt = (random.randint(1,2))
    if rikt == 1:
        foobar.left(45)
    else:
        foobar.right(45)
    foobar.forward(10)

turtle.mainloop()
