import random

#function for rollling the dies you roll two dies and you get their results in coordinates form 
def Roll():
    numbers=[1,2,3,4,5,6]
    x=random.choice(numbers)
    y=random.choice(numbers)
    return( x,y)

#definjing a function to control the interaction

def Play(x):
    if x=='y'or x=='Y':
        print(Roll(),"\n","->ROll the Die(Y/E)")

    elif x=='e' or x=='E':
        print ("->THANK YOU for playing GOODBYE")
    
    else:
        print("->invalid text try again")






#interact with the player
        
print ("hey  your name ")
name =input()
name =name.upper()


print("hello  ", name,"WELCOME to 'ROLLINGTHEDIE' which is a game of rolling the die ","\n","This is a basic outline of how to play the game ","\n","It uses TWO keywords","\n","1.Y for yes","\n","2.E for exiting the game")
print("Hope you have 'FUN'","\n","Lets START","\n","ROll the Die(Y/E)")
answer=input()

while answer!='e' or answer!='E' :
   
    print("Your results")
    Play(answer)
    answer=input()

if x=='e' or x=='E':
        print ("THANK YOU for playing GOODBYE")
    

