import turtle
# import random

turtle.Screen().bgcolor('gray')
# turtle.Screen().delay(1)

def turtest(turt,x,y,farg):
    turt = turtle.Turtle()
    turt.shape("turtle")
    turt.pencolor(farg)
    turt.goto(x,y)

screay = int(turtle.window_height() )
screax = int(turtle.window_width() )

foo=500
bar=500
turtest("foobar1",0,0,"red")
turtest("foobar2",0,bar,"red")
turtest("screaxx",screax/6,screay/6,"green")
turtest("barfoo1",-foo,-bar,"blue")
turtest("screayy",-screax/6,-screay/6,"yellow")
turtest("barfoo2",foo,0,"blue")

# def random_step(turtles):
#     turtles.forward(random.randint(5,15))
#     rikt = (random.randint(1,2))
#     if rikt == 1:
#         turtles.left(45)
#     else:
#         turtles.right(45)
#
# def border(turt):
#     for i in range(100):
#         y = int(turtle.window_height() )
#         x = int(turtle.window_width() )
#         turty=turt.ycor()
#         turtx=turt.xcor()
#         gox=-(turtx-100)
#         goy=-(turty-100)
#         # print(turtx,turty)
#         if turtx >= x or turtx <= -x:
#             turt.goto(-(gox),-(goy))
#         if turty >= y or turty <= -y:
#             turt.goto(-(gox),-(goy))
#
# while foobar.distance(barfoo) > 100:
#     random_step(foobar)
#     border(foobar)
#     random_step(barfoo)
#     border(barfoo)
#     y = int(turtle.window_height() )
#     x = int(turtle.window_width() )
#     print(f"x{x}\ny{y}\n")

print("Nära!")
turtle.mainloop()
