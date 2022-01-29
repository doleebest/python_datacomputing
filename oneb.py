from turtle import*

def diamond_flower (size=50, n=7, angle=30) :
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

diamond_flower()

goto(0,0)
clear()
up()
forward(200)
right(60)

for k in [7,9,11] : 
    for i in [5,k] : 
        diamond_flower(50, i, 360/i)
        right(60)
        up()
        forward(200)
    


        
    
        
