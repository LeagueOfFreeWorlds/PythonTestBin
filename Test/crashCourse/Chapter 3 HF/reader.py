
try:
    file = open('sketch.txt')
    for data in file:
        try:
            (role, line_spoken) = data.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except:
            pass
    file.close()
except:
    print("The data file is missing!")
