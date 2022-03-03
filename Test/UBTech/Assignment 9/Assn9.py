'''
@author:Nathan Igo
@date:03/02/2022
'''
from time import sleep

def main():
    userValue = 0
    userQuit = ''
    print("Welcome to the user log index.")
    print("We will start by having you enter your first name, last name.")
    nameF = str(input("Enter your first name:\t"))
    nameL = str(input("Enter your last name:\t"))
    name = (nameF + ' ' + nameL)
    fileWriter(name)
    print("Now that that's out of the way, feel free to add more user names, or check the current list of logs:\t")
    menuSelector()


def trueMeaning():
    # The computer needs to have a think...
    for i in range(5):
        print(".", end="")
        sleep(0.3)
    print()
    print("42.")

def fileWriter(user):
        user_data = open('userFile.txt', 'a')
        user_data.write(user)
        user_data.write('\n')
        user_data.close()
        # set the file to write several lines for a `list` type (Made pointless by bulkName()):
        '''elif type(user) is list:
            with open('userFile.txt', 'a') as userText:
                for line in user:
                    userText.write(line)
                    userText.write('\n')
                userText.close()'''



# File retriever is used for fetching users:
def fileRetriever():
    nameFind = str(input("Enter a name to search:\t"))
    with open('userFile.txt') as myFile:
        for num, line in enumerate(myFile, 1):
            if nameFind in line:
                print("Name has been located. ", nameFind)
                print('found at line:', num)


# Handles single names
def stringName():
    nameF = str(input("Enter first name:\t"))
    nameL = str(input("Enter last name:\t"))
    name = (nameF + ' ' + nameL)
    fileWriter(name)
def bulkName():
    count = 0
    users_length = eval(input("Enter the number of users that you want to add:\t"))
    for i in range(1, users_length + 1):
        count += 1
        firstName = str(input("Enter person " + str(count) + "'s first name:\t"))
        lastName = str(input("Enter person " + str(count) + "'s last name (leave blank if you don't want last name saved):\t"))
        Name = firstName + " " + lastName
        nameFile = open('userFile.txt', mode='a')
        nameFile.write(Name + "\n")
        nameFile.close()
def basePrint():
    user_data = open('userFile.txt', 'r')
    data_read = user_data.read()
    print(data_read)
    user_data.close()

# menuSelector handles user selections:
def menuSelector():
    exitVal = False
    while (exitVal == False):
        print("1.) Add another user.")
        print("2.) Bulk user add.")
        print("3.) Print Database to console.")
        print("4.) Search for user in user log.")
        print("5.) Quit the User Log Index program.")
        print("6.) Calculate the meaning of life... the universe... and everything!")
        user_select = eval(input("Enter a selection:\t"))
        if user_select == 1:
            stringName()
        elif user_select == 2:
            bulkName()
        elif user_select == 3:
            basePrint()
        elif user_select == 4:
            key = str("Enter name of user you want to look for:\t")
            fileRetriever()
        elif user_select == 5:
            print("Thanks for using the User Log Index.")
            exitVal = True
        elif user_select == 6:
            trueMeaning()




main()
