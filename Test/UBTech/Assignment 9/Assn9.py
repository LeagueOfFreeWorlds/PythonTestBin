'''
@author:Nathan Igo
@date:03/02/2022
'''
# WORK IN PROGRESS

def main():
    menuExecuter()

#TODO: Set the fileWriter to check and handle name lists.
def fileWriter(user):
    with open('userFile.txt', 'w') as userText:
        for line in user:
            userText.write(line)
            f.write('\n')



def fileRetriever(fileKey):

#Handles single names
def stringName(name):
    while (True):
        nameF = str(input("Enter first name:\t"))
        nameL = str(input("Enter last name:\t"))
        name = (nameF + ' ' + nameL)
        fileWriter(name)
        userQuit = str(input("Hit any key to continue adding names, or press \"n\" to finish."))
# Takes a name list, and appends it to the text.
def bulkName(names):

# menuExecuter mainly handles everything: 
def menuExecuter():
    userValue = 0
    userQuit = ''
    print("Welcome to the user log index.")
    print("We will start by having you enter your first name, last name.")
    nameF = str(input("Enter your first name:\t"))
    nameL = str(input("Enter your last name:\t"))
    name = (nameF + ' ' + nameL)
    fileWriter(name)
    print("Now that that's out of the way, feel free to add more user names, or ")




  

main()
