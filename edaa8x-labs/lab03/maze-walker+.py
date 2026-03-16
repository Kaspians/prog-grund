#!/bin/python3

#### PREP ####

# upg1
#
import maze
import turtle

maze_nr = int(input("maze, 1-5: "))
m = maze.Maze(maze_nr)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")

# NOTE: SPEED
turtle.Screen().delay(7)

# entry
x, y = m.entry()
pos_entry = (x, y)


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


# # print(m.wall_at_left(t.heading(), pos(t)))
# print("wall left, wall front", wall_left(t), wall_front(t), "\n")

while not m.at_exit(t.pos()):
    if not wall_front(t) and wall_left(t):
        # print("move time !!")
        while wall_left(t) and not wall_front(t):
            # print("forward")
            t.forward(1)
        # print("end of while")
        # checko höger om vägg vänster
        t.left(90)
        if not wall_front(t):
            t.forward(1)
        else:
            t.right(180)
    else:
        # print("wall front")
        t.left(90)

print("done")


turtle.mainloop()
