import math
from turtle import*
import random

def DrawingHeart(bgColor ,Color,sizeX,sizeY):
    def HeartX(x):
        return sizeX*math.sin(4*(math.pi()*2))
    def HeartY(x):
        return sizeY*math.cos(4*(math.pi()*2))

    speed(80000000000)
    bgcolor(bgColor)
    color(Color)
    
    

    for i in range(360):
        goto(HeartX(math.radians(i)),HeartY(math.radians(i)))
        

def DrawingDon(color,X,Y):
    turtle.pensize(10)
    def Xaxis(x):
        return (x)
    def Yaxis(y):
        return y
    goto(math.radians(X),math.radians(Y))

colors =["red","white","black","blue","grey","pink","gold"]


for i in (5,8,1):
    Color=random.choice(colors)
    bgColor=random.choice(colors)
    DrawingHeart(bgColor,Color,i,i+1)
done()
    
