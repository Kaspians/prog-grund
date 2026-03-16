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
turtle.Screen().delay(0)

# entry
x, y = m.entry()
pos_entry = (x, y)
# print(f"pos_entry={pos_entry}")


# function pos
def pos(padda):
    return (padda.xcor(), padda.ycor())


# # start padda pos
# print(f"pos t={pos(t)}")

# padda goto entry
t.penup()
t.goto(x, y)
t.pendown()

#### START ####


def wall_front(padda):
    return m.wall_in_front(padda.heading(), pos(t))


def wall_left(padda):
    return m.wall_at_left(padda.heading(), pos(t))


# # print(m.wall_at_left(t.heading(), pos(t)))
# print("wall left, wall front", wall_left(t), wall_front(t), "\n")

while not m.at_exit(pos(t)):
    if wall_front(t) is False and wall_left(t) is True:
        # print("move time !!")
        while wall_left(t) is True and wall_front(t) is False:
            # print("forward")
            t.forward(1)
        # print("end of while")
        # FIXME: checko höger om vägg vänster
        t.left(90)
        if wall_front(t) is False:
            t.forward(1)
    else:
        # print("wall front")
        t.left(90)

print("done")


turtle.mainloop()
