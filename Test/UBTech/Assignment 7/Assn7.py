'''
@author: Nathan Igo
@date: 02-03-2022
'''
def main():
    entry()
def passwordWriter(passCode):
    for p in passCode:
        print ("Password saved successfully." if passCode.isalnum() else "Please enter alphanumeric characters only.")
def entry():
    pw = str(input("Enter your password. Use alphanumeric characters only:\t"))
    passwordWriter(pw)
main()
