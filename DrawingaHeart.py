import math #this is for importing the neccersary functions
from turtle import*
import random

#defining a function for drawing a heart  
def heart1(x):
    return 10*math.sin(x)**3
def heart2(x):
    return 5*math.cos(x)-2*math.cos(2*x)-2*math.cos(3*x)-math.cos(4*x)

speed(100000**300000)


#this is where we call the funtion to draw the heartshape
#this a loop for drawing



for i in range(360):
    
    bgcolor("black")
    color("red")
    
    goto(heart1(math.radians(i))*20,heart2(math.radians(i))*20)#moving turtle to the  spesified location to start drawing
    
    for j in range(10):
        
        goto(0,0)
        
for i in range(360):
    
    bgcolor("white")
    color("blue")
    
    goto(heart1(math.radians(i))*20,heart2(math.radians(i))*20)#moving turtle to the  spesified location to start drawing
    
    for j in range(10):
        
        goto(0,0)
for i in range(360):
    
    bgcolor("red")
    color("white")
    
    goto(heart1(math.radians(i))*20,heart2(math.radians(i))*20)#moving turtle to the  spesified location to start drawing
    
    for j in range(10):
        
        goto(0,0)
        


    
done()
