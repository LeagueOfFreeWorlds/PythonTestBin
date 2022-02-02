'''
Bookmenu is the menu for the booksaverprogram. It simply contains
the menu items, along with the menu functions in the modules
directory.
'''

from modules.bookfilesys import *
def bookMenu():
    running = True
    book = ''
    while running:
        print("1. Read your bookshelf")
        print("2. Write a book to your bookshelf")
        print("3. Quit")
        selection = eval(input("What will it be?\t"))
        if selection == 1:
            bookReader()
        elif selection == 2:
            book = input("Enter your book name:\t")
            bookwriter(book)
        elif selection == 3:
            print("See ya!")
            running = False
