from turtle import *
width(10)
shape("turtle")
setposition(-100,0)
n=int(input("Number of dash : "))
for i in range (n):
    if i % 6 <3 :
        color("blue")
    else:
        color("red")
    forward(15)
    penup()
    forward(15)
    pendown()
mainloop()
