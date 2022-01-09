'''
@author: Nathan Igo
@date: 1/6/2022
'''
def main():
    print("Welcome to account creation wizard. Please follow the instructions below to get your account created.")
    print("We will be asking for your first and last name, your user name, and a 3 character password.")
    getUserSummary()

#///////// SETTTERS: /////////////////////////////////////////
def setName():
    FirstName = input("Please enter your first name.\t")
    LastName = input("Please enter your last name.\t")
    name = FirstName, LastName
    return name

def setUserName():
    userName = input("Please enter your username:\t")
    return userName
#/////////////////////////////////////////////////////////////
def passCreate():
    check = False
    error = False
    while check == False:
        error = False
        password = str(input("Plase enter your password (three numerical characters ONLY!):\t"))
        for i in password:
            if ord(i) < 48 or ord(i) > 57 and error == False:
                print("Please enter numerical values only.")
                error = True
        if len(password) > 3 and error == False:
            print("A password can only be up to 3 characters long. Please try again.")
            error = True
        elif error == False:
            print("Password created successfully:\t", password)
            check = True

def getUserSummary():
    first, last = setName()
    usern = setUserName()
    passCreate()
    print(first, last, usern)

main()
