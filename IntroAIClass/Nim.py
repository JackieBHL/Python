#nim.py
#CSE 5120


import random

def nim_setup(k):
    mynim = [k,k,k]
    return mynim

def show_nim(nim):
    for i in range(3):
        print ("Pile %d: " % (i+1),end='')
        for i in range(nim[i]):
            print("0 ",end='')
        print("")
    print("\n") 
    return

def play_nim(k):
    game = nim_setup(k)
    show_nim(game)
    x=0
    player_moves(game)
    while game != [0,0,0]:
        print("These piles of stone remain .... Continue to play")
        show_nim(game)
        if x==1:
            player_moves(game)
            x=0
        else:
            computer_moves(game)
            x=1
    show_nim(game)
    if x==1:
        print("Computer took the last stone....Player Wins")
    else:
        print("Player took the last stone .... Computer Wins")
    return

def player_moves(nim):
    inrange = False
    enough = False
    while inrange == False:
        choosepiles = input('Choose Pile [1-3]: ')
        choosepile = int(choosepiles)
        if choosepile <=3 & choosepile>=0:
            inrange = True
            break
        print("Choose from Pile [1-3] : %d is not a vaild pile: " % choosepile)
    while enough==False:
        takeaways = input("You take how many stones form pile %d? " % choosepile)
        takeaway = int(takeaways)
        if takeaway <= nim[choosepile-1]:
            enough=True
            break
        print("There aren't enough stone!")
    print("You took %d stone(s) from pile %d" % (takeaway, choosepile))

    nim[choosepile-1] = nim[choosepile-1]- takeaway
    return

def computer_moves(nim):
    pile = random.randint(1,3)
    while nim[pile-1] == 0:
        pile = random.randint(1,3)
    
    take = random.randint(1,nim[pile-1])

    print("Computer took %d stone(s) from pile %d" % (take, pile))
    nim[pile-1] = nim[pile-1] - take
    return


if __name__ == '__main__':
    numberofstones =  5 #input("Enter Stone Number: ")
    print("Three piles of %s stones ... Start the Game!" % numberofstones)
    numberofstones = int(numberofstones)
    play_nim(numberofstones)
    


