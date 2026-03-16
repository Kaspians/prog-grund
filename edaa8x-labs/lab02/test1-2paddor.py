import turtle
# import random

turtle.Screen().bgcolor('gray')
turtle.Screen().delay(5)

def turmake(name,x,y,farg):
    name = turtle.Turtle()
    name.shape("turtle")
    name.pencolor(farg)
    name.goto(x,y)

screay = int(turtle.window_height() )
screax = int(turtle.window_width() )

def window_what():
    screay = int(turtle.window_height() )
    screax = int(turtle.window_width() )
    print(f"screax {screax}")
    print(f"screay {screay}")

window_what()

foo=500
bar=500
turmake("foobar1",0,0,"red")
turmake("foobar2",0,bar,"red")
turmake("screaxx",screax/6,screay/6,"green")
turmake("barfoo1",-foo,-bar,"blue")
turmake("screayy",-screax/6,-screay/6,"yellow")
turmake("barfoo2",foo,0,"blue")

while True:
    window_what()

print("Nära!")
turtle.mainloop()
