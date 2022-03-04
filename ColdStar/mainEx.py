'''
@author: Nathan Igo
@date: 03-04-2022
'''
# sleep module slows game down when invoked
from time import sleep
## The job of the main function is to start the game, as well as display a menu for the user:
def main():
    ## Menu selection
    print("Welcome to ColdStar! Select an option below.")
    print()
    print("1. Start a new game")
    sleep(0.2)
    print("2. Check leaderboard")
    sleep(0.2)
    print("3. Quit ColdStar")


def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()


main()