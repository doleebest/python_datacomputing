from turtle import *

def diamond_flower (size=100, n=7, angle=30) :
    down()
    for i in range(n) :
        for j in range(2) :
            forward(size)
            right(angle)
            forward(size)
            right(180-angle)
        right(360/n)
    up()

speed(0)
delay(0)
up()

for i in range (10) :
    if (i in {2,3,7}) :
        color (0,0,1)
    else :
        color(0,0,0)
    diamond_flower(size=20)
    forward(80)
    
            
