#!/bin/python3
#
# turtle_walk

# 4
#
import turtle
import random
foobar=turtle.Turtle()
def random_step(turtles):
    turtles.forward(random.randint(5,15))
    rikt = (random.randint(1,2))
    if rikt == 1:
        turtles.left(45)
    else:
        turtles.right(45)

def random_walk(turtlew,n):
    for i in range(n):
        random_step(turtlew)

foobar.shape("turtle")
foobar.pencolor("green")
random_walk(foobar,100)

turtle.mainloop()

# 5
#
# import turtle
# import random
# foobar=turtle.Turtle()
# def random_step(turtles,a,b):
#     turtles.forward(random.randint(a,b))
#     rikt = (random.randint(1,2))
#     if rikt == 1:
#         turtles.left(45)
#     else:
#         turtles.right(45)
#
# def random_walk(turtlew,n,a,b):
#     for i in range(n):
#         random_step(turtlew,a,b)
#
# random_walk(foobar,100,5,100)
#
# turtle.mainloop()
