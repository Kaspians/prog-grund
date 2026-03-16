#!/bin/python3

##############
## Bakgrund ##
##############

import maze
import turtle

# maze_nr = int(input("maze, 1-5: "))
maze_nr = 1
m = maze.Maze(maze_nr)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")

x, y = m.entry()
pos_entry = (x, y)
print(pos_entry)

pos_t = t.pos()

q_exit = m.at_exit(pos_t)

print(m.entry())
print(pos_t)
print(q_exit)

turtle.mainloop()

############
## Tupler ##
############
# list = ["a",2,"foobar","tuple"]
# tuple = ("a',2,"barfoo","tuple")
#
# padda = turtle.Turtle()
#
# pos = padda.entry()
#
# function cur_pos(turt):
#   return [turt.xcor(),turt.ycor()]
# pos = (padda.xcor(),padda.ycor())
#
# padda.at_exit(pos)
#
#############
## SCRATCH ##
#############
