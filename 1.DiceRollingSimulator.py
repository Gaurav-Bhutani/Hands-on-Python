import random

def fun():
    play = True
    while play:
        die=random.randint(1,6)
        print("Generated number is: ",die)
        temp=input("Press enter to roll die again  or  Press 0 to exit:\t")
        if(temp=='0'):
            play = False

player=input('Please enter your name: ')
print("\nHello " + player + "...!!")
print("\nThis game will randomly generate any number between 1 and 6 by rolling a die\n")

fun()