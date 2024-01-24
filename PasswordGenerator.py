import string
import random

Length = int(input('Enter password Length: '))

print('''Choose the characters you want to use in your password:
         1. Letters
         2. Digits
         3. Special characters
         4. Exit''')  # input what characters you want in it, for example, if you want only letters, put 1 and then 4

characterList = ""

while True:
    choice = int(input('Pick a number: '))

    if choice == 1:
        characterList += string.ascii_letters  # This has only letters[a,b,c,e,...].
    elif choice == 2:
        characterList += string.digits  # This only has digits[1,2,5,96,...].
    elif choice == 3:
        characterList += string.punctuation  # This only has special characters[#, &, (), [], .,...]
    elif choice == 4:
        break
    else:
        print('Invalid input. Please choose a valid option.')  # This is printed when your choice is not 1, 2, 3 or 4.

password = []

for i in range(Length):
    randomChar = random.choice(characterList)
    password.append(randomChar)

print("The random password is " + "".join(password))  # Prints your password.
