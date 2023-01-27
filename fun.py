#on peut tout faire avec python !
#:joy:


import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")

star = turtle.Turtle()

for i in range(50):
    star.color(random.random(), random.random(), random.random())
    star.forward(i * 10)
    star.right(144)

wn.mainloop()
