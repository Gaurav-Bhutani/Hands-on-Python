def fun():
    play = True
    while play:
        print("Please complete the Story:")
        s1=input("1. Please enter a noun:\t")
        s2=input("2. Please enter a pronoun:\t")
        s3=input("3. Please enter a noun:\t")
        s4=input("4. Please enter a noun:\t")
        s5=input("5. Please enter a noun:\t")
        s6=input("6. Please enter a noun:\t")
        s7=input("7. Please enter a verb:\t")
        print("\nThe story made by you is:\n")
        print(s1 +" is fat. So, " + s2 + " is running. To become " + s3 + ". Then " + s4 + " become hungry. After eating " + s5 + " , " + s6 + " is " + s7 + " .\n")
        temp=input("Press ENTER if you want to play again  or  Press 0 to exit:\t")
        if(temp=='0'):
            play = False

player=input('Please enter your name: ')
print("\nHello " + player + "...!!\n")
print("This game is based on Mad libs.")
print("In this game we have to complete a story by filling proper Noun, Adjective, Verb, etc.\n")

fun()
