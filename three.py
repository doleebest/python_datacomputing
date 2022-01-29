from turtle import*

def diamond_flower (size=50, n=7, angle=30) :
    down()
    for i in range (n) :
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


goto(-400,0)
L = [ (3,70), (5,50), (9,50), (9,30), (30,10) ]
for (n, angle) in L :
    diamond_flower(50,n,angle)
    forward(200)
    
