'''
@author: Nathan Igo
@date: 02/26/2022
'''


from random import randint

#create a list of play options

#assign a random play to the computer
print("Welcome to GNU/Linux/Windows... Just like Rock Paper Scissors, but with a twist!")
name = str(input("Let's start with a name. What shall we call you?\t"))

# Random win chance:
def winRand():
    win = False
    a = randint(0, 1)
    if(a == 0):
        win = True
    else:
        win = False
    return win

playerLives = 4
rounds = 0;
t = ["GNU", "Linux", "Windows"]
while playerLives != 0:
    # Generate random input for the computer:
    computer = t[randint(0, 2)]
    #set player to True
    print("What will it be " + name + "?")
    player = input("GNU, Linux, Windows?\t")
    winBool = winRand()
    if player == computer:
        print("Tie!")
        rounds+=1
    elif player == "GNU":
        if computer == "Windows":
            print("You lose!", computer, "mistreats", player)
            playerLives-=1
            print("Lives left:\t" + str(playerLives))
        else:
            print("You win!", player, "deprives", computer)
            rounds+=1
            print("Rounds passed:\t" + str(rounds))
            if winBool == True:
                print("You won an additional life!")
                playerLives+=1
    elif player == "Linux":
        if computer == "GNU":
            print("You lose this round!", computer, "decompiles", player)
            playerLives-=1
            print("Lives left:\t" + str(playerLives))
        else:
            print("You win!", player, "shatters", computer)
            rounds+=1
            print("Rounds passed:\t" + str(rounds))
            if winBool == True:
                print("You won an additional life!")
                playerLives+=1
    elif player == "Windows":
        if computer == "Linux":
            print("You lose...", computer, "shatters", player)
            playerLives-=1
            print("Lives left:\t" + str(playerLives))
        else:
            print("You win!", player, "monetizes", computer)
            rounds+=1
            print("Rounds passed:\t" + str(rounds))
            if winBool == True:
                print("You won an additional life!")
                playerLives+=1
    else:
        print("That's not a valid play. Check your spelling!")
    computer = t[randint(0,2)]

if rounds >= 4:
    print("You survived " + str(rounds) + " consecutive rounds! Congrats, " + str(name) + "!")
else:
    print("You didn't survive more than 3 rounds. You lost!")

