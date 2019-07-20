import random

movies=['INCREDIBLES','JUNGLE BOOK','KUNG FU PANDA','DESPICABLE ME','MINIONS','TOY STORY','ICE AGE','ALADDIN','FINDING NEMO','TARZEN','FROZEN','BIG HERO','POKEMON']

def is_present(letter,movie):
    temp=movie.count(letter)
    if temp=='0':
        return False
    else:
        return True

def unlock(qn,n,letter):
    ref=list(n)
    qn_list=list(qn)
    temp=[]
    num=len(n)
    for i in range(num):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new

def fun():
    score=0
    play=True
    while play:
        guess=8
        print('Number of times you can guess the letters of the word is: '+str(guess)+'\n')
        n=random.choice(movies)
        qn=len(n)
        letters=list(n)
        temp=[]
        for i in range(qn):
            if letters[i]==' ':
                temp.append(' ')
            else:
                temp.append('*')
        qn=''.join(str(x) for x in temp)
        print(qn)
        Edited_qn=qn
        letter=input('Your letter: ')
        trying=True
        while trying:
            guess=guess-1
            if guess==0:
                print('\nSorry..!!\nYour chances to guess the movie is over.')
                trying=False
                temp=input('Press Enter to play again or Press 0 to Exit: ')
                if temp=='0':
                    print("\nThanks for playing...\nYour Score is: "+str(score))
                    play=False
            else:
                print('\nNumber of times you can guess the letters of the word is: '+str(guess))
                if(is_present(letter,n)):
                    #unlock
                    Edited_qn=unlock(Edited_qn,n,letter)
                    print(Edited_qn)
                    letter=input('Your letter: ')
                    if Edited_qn==n or letter==n:
                        print('Correct')
                        score = score+1
                        trying=False
                        temp=input('Press Enter to play again or Press 0 to Exit: ')
                        if temp=='0':
                            print("\nThanks for playing...\nYour Score is: "+str(score))
                            play=False

player=input('Please enter your name: ')
print("\nHello " + player + "...!!\n")
print("Welcome to the Hangman.")
print("In this game you have to guess the movie.\n")
print("You can enter only one letter at a time or the full name of the movie.\n")
fun()