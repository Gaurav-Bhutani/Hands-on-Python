import random

def fun():
    room=random.randint(1,6)
    
    play = True
    while play:
        #Room 1
        if(room==1):
            print("\nYou are in Room number:\t" + str(room) + "\nIt's colour is Red.")
            temp=input('Please enter your choice in which direction you want to move:\t')
            if(temp=='r' or temp=='R'):
                room=2
            elif(temp=='u' or temp=='U'):
                room=4
            elif(temp=='l' or temp=='L'or temp=='d' or temp=='D'):
                temp=input('Sorry..!!\nYou can not move in this direction because their is a wall.\nPlease try to move in different direction.\nPress ENTER to Continue... or Press 0 to Exit:\t')
            else:
                temp=input('You entered wrong option.\nPress ENTER to Continue... or Press 0 to Exit:\t')
        
        #Room 2
        if(room==2):
            print("\nYou are in Room number:\t" + str(room) + "\nIt's colour is Yellow.")
            temp=input('Please enter your choice in which direction you want to move:\t')
            if(temp=='l' or temp=='L'):
                room=1
            elif(temp=='u' or temp=='U'):
                room=3
            elif(temp=='r' or temp=='R' or temp=='d' or temp=='D'):
                temp=input('Sorry..!!\nYou can not move in this direction because their is a wall.\nPlease try to move in different direction.\nPress ENTER to Continue... or Press 0 to Exit:\t')
            else:
                temp=input('You entered wrong option.\nPress ENTER to Continue... or Press 0 to Exit:\t')

        
        #Room 3
        if(room==3):
            print("\nYou are in Room number:\t" + str(room) + "\nIt's colour is Blue.")
            temp=input('Please enter your choice in which direction you want to move:\t')
            if(temp=='d' or temp=='D'):
                room=2
            elif(temp=='u' or temp=='U'):
                room=6
            elif(temp=='l' or temp=='L'):
                room=4
            elif(temp=='r' or temp=='R'):
                temp=input('Sorry..!!\nYou can not move in this direction because their is a wall.\nPlease try to move in different direction.\nPress ENTER to Continue... or Press 0 to Exit:\t')
            else:
                temp=input('You entered wrong option.\nPress ENTER to Continue... or Press 0 to Exit:\t')
        
        #Room 4
        if(room==4):
            print("\nYou are in Room number:\t" + str(room) + "\nIt's colour is Green.")
            temp=input('Please enter your choice in which direction you want to move:\t')
            if(temp=='r' or temp=='R'):
                room=3
            elif(temp=='u' or temp=='U'):
                room=5
            elif(temp=='d' or temp=='D'):
                room=1
            elif(temp=='l' or temp=='L'):
                temp=input('Sorry..!!\nYou can not move in this direction because their is a wall.\nPlease try to move in different direction.\nPress ENTER to Continue... or Press 0 to Exit:\t')
            else:
                temp=input('You entered wrong option.\nPress ENTER to Continue... or Press 0 to Exit:\t')
        
        #Room 5
        if(room==5):
            print("\nYou are in Room number:\t" + str(room) + "\nIt's colour is Violet.")
            temp=input('Please enter your choice in which direction you want to move:\t')
            if(temp=='r' or temp=='R'):
                room=6
            elif(temp=='d' or temp=='D'):
                room=4
            elif(temp=='l' or temp=='L' or temp=='u' or temp=='U'):
                temp=input('Sorry..!!\nYou can not move in this direction because their is a wall.\nPlease try to move in different direction.\nPress ENTER to Continue... or Press 0 to Exit:\t')
            else:
                temp=input('You entered wrong option.\nPress ENTER to Continue... or Press 0 to Exit:\t')
                
        #Room 6
        if(room==6):
            print("\nYou are in Room number:\t" + str(room) + "\nIt's colour is Pink.")
            temp=input('Please enter your choice in which direction you want to move:\t')
            if(temp=='l' or temp=='L'):
                room=5
            elif(temp=='d' or temp=='D'):
                room=3
            elif(temp=='r' or temp=='R' or temp=='u' or temp=='U'):
                temp=input('Sorry..!!\nYou can not move in this direction because their is a wall.\nPlease try to move in different direction.\nPress ENTER to Continue... or Press 0 to Exit:\t')
            else:
                temp=input('You entered wrong option.\nPress ENTER to Continue... or Press 0 to Exit:\t')
        
        if(temp=='0'):
            play = False

player=input('Please enter your name: ')
print("\nHello " + player + "...!!\n")
print("This is an Adventure game.")
print("In this game you have to travel through the rooms of the house.\n")
print("Their are 6 room in the house.\n")

print("To move Up press:\tU / u")
print("To move Down press:\tD / d")
print("To move Left press:\tL / l")
print("To move Right press:\tR / r")

fun()