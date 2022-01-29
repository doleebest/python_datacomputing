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
    up()

speed(0)
delay(0)
up()

flower_dict = { 'trigems':(3,70), 'five':(5,50), 'richnine':(9,50), 'thinnine':(9,30), 'needle':(30,10)}    

while True :
    name = input('Enter flower name ')
    if name in flower_dict :
        (n,angle) = flower_dict[name]
        clear()
        diamond_flower(n=n, angle=angle)
    else :
        name = input('error ; Enter flower name correctly ')
        (n,angle) = flower_dict[name]
        clear()
        diamond_flower(n=n, angle=angle)

        

    
