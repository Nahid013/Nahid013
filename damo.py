from turtle import *
from random import randint

speed(100)

bgcolor('black')

x = 1

while x <550:
    r= randint(0,255)
    g= randint(0,255)
    b= randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    fd(10+x)
    rt(130.900)
    x+=1
    
exitonclick( )