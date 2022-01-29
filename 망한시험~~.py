from turtle import *

def diamond_flower (size=50, n=7, angle=30) :
    down()
    for i in range(n) :
        for j in range(2)  :
            forward(size)
            right(angle)
            forward(size)
            right(180-angle)
        right(360/n)
    up()

speed(0)
delay(0)


flower_dict = {'trigems':(3,70), 'five':(5,50)}


while True :
    key = input("Enter flower name  ")
    if key in flower_dict :
        (n,angle) = flower_dict[key]
        diamond_flower(100,n,angle)
    else :
        key2 = input("Enter flower name correctly  ")
        (n,angle) = flower_dict[key2]
        diamond_flower(100,n,angle)
