'''
@author: Nathan Igo
@date: 02-02-2022
'''
def main():
    numEntry = str(input("Enter your phone number (DO NOT USE \"-\"):\t"))
    print(prefix(numEntry))

# Locates and prints the prefix:
def prefix(num):
    pref = []
    for i in range(3, 6):
        pref.append(num[i])
    return "Prefix is: " + ''.join(pref)
main()