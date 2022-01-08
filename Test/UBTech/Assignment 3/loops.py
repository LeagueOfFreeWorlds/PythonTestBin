'''
@author: Nathan Igo
@date: 1/6/2022
'''
'''PassWord = ''
FirstName = ''
LastName = ''
UserName = '''
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
    check == False;
    while check == False:
        password = input("Plase enter your password (three numerical characters ONLY!):\t")
        for i in password:
            if password[i] == type(str):
                print("Please enter numerical values only.")
                break
        if len(password) > 3:
            print("A password can only be up to 3 characters long. Please try again.")
            break
        else:
            print("Password created successfully:\t", password)

def getUserSummary():
    setName() = fist, last
    setUserName() = usern
    print(first, last, usern)

main()
