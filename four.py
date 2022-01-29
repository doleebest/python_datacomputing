from turtle import*

def diamond_flower(size=50, n=7, angle=30 ) :
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

flower_dict = { 'trigems':(3,70), 'five':(5,50), 'richnine':(9,50), 'thinnine':(9,30), 'needle':(30,10)}

def draw(name) :
    clear()
    (n,angle) = flower_dict[name]
    diamond_flower(100,n,angle)
    

