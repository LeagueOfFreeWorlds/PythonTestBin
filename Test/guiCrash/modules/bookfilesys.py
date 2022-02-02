'''
the bookwriter program is responsible for ensuring that code
is written and stored on the computer system. It will be comprised
of two functions.
'''
# def bookwritingSelection(book='', author=''):


def bookwriter(book):
    book_list = open("booklist.txt", "a")
    book_list.write(str(book) +"\n")
    book_list.close()

def bookReader():
    # "r" means the file is for reading purposes only.
    r = open("booklist.txt", "r")
    lines = r.readlines()
    for line in lines:
        print(line, end='')


