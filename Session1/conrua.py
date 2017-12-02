Maze
from turtle import *
color("red")
shape("classic")
speed(-1)
for i in range (1000):
    forward(i)
    left(90)
    forward(i+i)
mainloop()

Dash
from turtle import *
shape("classic")
speed(-1)
for i in range(10):
    forward(30)
    penup()
    forward(30)
    pendown()
mainloop()
