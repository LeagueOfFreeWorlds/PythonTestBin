'''
Secret password creator.
'''
passwordFile = open('cekretpassword.txt')
secretPassword = passwordFile.read()
typedPassword = input("Enter your password:\t")
if typedPassword == secretPassword:
    print("Password correct.")
    if typedPassword == '12345':
        print("That password is what idiots put on their luggage.")
else:
    print("Password incorrect.")
