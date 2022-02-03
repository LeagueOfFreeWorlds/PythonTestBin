'''
@author: Nathan Igo
@date:   2, 1, 2022
'''
from time import sleep
firstTime = True
def main():
    done = False
    print("Welcome to Name Saver. As a courtesy, you will have to enter your name if you wish to see the list of names available.")
    nameWriter()
    while not done:
        print()
        print("MENU")
        print("1)\tEnter Another Name")
        print("2)\tSee List of Names")
        print("3)\tSearch For a Name")
        print("4)\tQuit")
        mode = int(input("Enter a selection:\t"))
        if mode == 1:
            nameWriter()
        elif mode == 2:
            nameReader()
        elif mode == 3:
            nameLookup()
        elif mode == 4:
            done = True
            break
        else:
            print("Sorry, an input error has occured. Please try again.")

# Objects dedicated to reading and writing, such that it doesn't clutter the main function:
# Mmm... Melikes OOP :-)
def nameWriter():
    global firstTime
    if not firstTime:
        print("1. Single add | 2. Bulk add.")
        bulkName = int(input("Select whether you're doing one name, or bulk naming (adding multiple people):\t"))
        if bulkName == 1:
            firstName = str(input("Enter your first name:\t"))
            lastName = str(input("Enter your last name (leave blank if you don't want last name saved):\t"))
            Name = firstName + " " + lastName
            nameFile = open('nameList.txt', mode='a')
            nameFile.write(Name + "\n")
            nameFile.close()
        elif bulkName == 2:
            count = 0
            bulkAmount = int(input("What is the number of people that you're entering? (ENTER A VALUE):\t"))
            for i in range(1, bulkAmount + 1):
                count += 1
                firstName = str(input("Enter person " + str(count) + "'s first name:\t"))
                lastName = str(input("Enter person " + str(count) + "'s last name (leave blank if you don't want last name saved):\t"))
                Name = firstName + " " + lastName
                nameFile = open('nameList.txt', mode='a')
                nameFile.write(Name + "\n")
                nameFile.close()
        else:
            print("Sorry, an input error has occured. Please try again.")
    else:
        firstName = str(input("Enter your first name:\t"))
        lastName = str(input("Enter your last name (leave blank if you don't want last name saved):\t"))
        Name = firstName + " " + lastName
        nameFile = open('nameList.txt', mode='a')
        nameFile.write(Name + "\n")
        nameFile.close()
        firstTime = False


def nameReader():
    print("Opening now")
    thinking()
    nameFile = open('nameList.txt', mode='r')
    nameIndex = nameFile.read()
    print(nameIndex)
    nameFile.close()
def nameLookup():
    nameFind = str(input("Enter a name to search:\t"))
    thinking()
    with open('nameList.txt') as myFile:
        for num, line in enumerate(myFile, 1):
            if nameFind in line:
                print("Name has been located. ", nameFind)
                print('found at line:', num)





## Little animation that I developed:
def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.3)
    print()

main()
