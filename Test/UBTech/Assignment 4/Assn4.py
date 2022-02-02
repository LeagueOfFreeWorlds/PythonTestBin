'''
@author: Nathan Igo
@ date: 1-10-2022
'''
running = True
while running:
    running = True
    NameList = []
    FirstName = str(input("Enter your first name:\t"))
    LastName = str(input("Enter your last name:\t"))
    Name = FirstName + LastName
    if not (64 < ord(FirstName[0]) < 91):
        print("Please capitalize the first letter in your First Name.")
    elif not (64 < ord(LastName[0]) < 91):
        print("Please capitalize the first letter in your Last Name.")
    else:
        for i in Name:
            NameList.append(ord(i))
        if all([65 <= i <= 122 and not (91 <= i <= 96) for i in NameList]):
            print("Name entered successfully.\t", FirstName + " " + LastName)
            running = False
        else:
            print("Please only use Letters when entering your name.")
            print("Sorry X Æ A-Xii.")
