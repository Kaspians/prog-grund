#!/bin/python3

#### PREP ####

import turtle

# upg1
#
import maze

maze_nr = int(input("maze, 1-5: "))
turt_speed = int(input("How fast (0 is fastest): "))

m = maze.Maze(maze_nr)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")

# entry
x, y = m.entry()
pos_entry = (x, y)

turtle.Screen().delay(turt_speed)


# # function pos
# def pos(padda):
#     return (padda.xcor(), padda.ycor())


# # start padda pos
# print(f"pos t={pos(t)}")

# padda goto entry
t.penup()
t.goto(x, y)
t.pendown()

#### START ####


def wall_front(padda):
    return m.wall_in_front(padda.heading(), t.pos())


def wall_left(padda):
    return m.wall_at_left(padda.heading(), t.pos())


while not m.at_exit(t.pos()):
    if not wall_front(t) and wall_left(t):
        while wall_left(t) and not wall_front(t):
            t.forward(1)
        # if wall_left(t) and wall_front(t):
        if wall_left(t):
            t.right(90)
        elif not wall_left(t):
            t.left(90)
            t.forward(1)
        else:
            t.left(90)
    else:
        # print("wall front")
        t.left(90)

print("done")


turtle.mainloop()
