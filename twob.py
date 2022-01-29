from turtle import*

def diamond_flower(size=50, n=7, angle=30) :
    down()
    for i in range(n) :
        for j in range(2) :
            forward(size)
            right(angle)
            forward(size)
            right(180-angle)
        right(360/n)

speed(0)
delay(0)
up()

goto(0,200)
L = [ [3,70], [5,50], [9,50], [30,10], [9,30] ]
for flower in L*3 :
    diamond_flower(25, flower[0], flower[1])
    up()
    forward(100)
    right(120/5)
up()

    
    
