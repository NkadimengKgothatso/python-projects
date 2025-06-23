import random

#interact with the player
        
print ("hey  your name ")
name =input()
name =name.upper()


print("hello  ", name,"WELCOME to NUMBERGUESSING which is a game of guessing a number the cumputor chose ","\n","This is a basic outline of how to play the game ","\n","-you just guess a number ","please note that the numbers are less or equal to 50","\n","-the computer will give you these hints untill you get it right","\n","'too high' or 'too low' ","\n","to exit the game press E")
print("Hope you have 'FUN'","\n")


number=input()

    
Cnum=random.randint(1,50)


while number!='E'or number != 'e':
    if int(number)==Cnum:
        print("congrats your correct")
    elif int(number)>Cnum:
        print("too high try again")
    elif int(number)<Cnum:
        print("too low try again ")
    elif number=='E' or number =='e' :
        print("Thank you for playing ")
        break
  
    else:
        print("invalid text try again")
        
    number=input("GUESS A NUMBER-")
    if str(number)=='E' or str(number) =='e' :
        print("Thank you for playing ")
    

      
