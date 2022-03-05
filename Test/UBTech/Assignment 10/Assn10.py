'''
@author: Nathan Igo
@date: 03/4/22
'''
from random import randint
from time import sleep
def main():
    done = False
    print("Welcome to Hangman, please make a selection:")
    print()
    ## Program will continue to run so long as it is not done, unless the user wishes to quit:
    while(not done):
        print("Please make a selection:\t")
        print("1. Play Hangman")
        print("2. Check leaderboard")
        print("3. Quit Hangman")
        selection = eval(input("Enter a selection:\t"))
        # Selection 1 will turn the program over to the hangGame() method, which will be where the actual game is
        # displayed and the user can begin to make guesses:
        if selection == 1:
            hangGame()
        elif selection == 2:
            getLeaderboard()
        elif selection == 3:
            print("Thanks for playing!")
            done = True
        else:
            print("Sorry man, I have no idea what you entered. Please try again.")

def thinking():
    for i in range(5):
        print(".", end='')
        sleep(0.1)
    print()

'''def searchAlg(wordList, key):
    for letter in wordList:
        if letter == key:'''


## Library of random words:
def randWord():
    wordList = ["Alphanumeric", "Arch Linux", "Asymmetric", "Balance", "Calculate", "Data", "Entertain", "FreeBSD",
                "General", "Hypertext", "Intelligentsia", "Janky", "Kool Desktop Environment", "Language", "Noctua",
                "Operation", "ThinkPad"]
    wordSelected = wordList(randint(0, len(wordList)))
    return wordSelected

def getLeaderboard():
    print("Test")

def hangGame():
    print("Generating random word. Please wait...")
    word = randWord()
    emptyArray = []
    ## Create an empty array that represents the length of the word that has been generated:
    for i in len(word):
        emptyArray[i].append("_")
    solved = False
    # We then want to convert our word to a list, because we then need to check if a letter entered matches a letter
    # in the word:
    wordSplitted = word.split()
    # Now for the loop. The user will have to continue to guess until all of the letters are present:
    while (not solved):
        print(emptyArray)
        user_key = str(input("Enter a letter to guess:\t"))
        for j in wordSplitted:
            for array_index in len(wordSplitted):
                if user_key == j:
                    emptyArray[array_index].insert(j)
        if not ("_" in emptyArray):
            solved = True
main()