import random

name = input('What is your name? ')
print('Hello', name, 'try and guess my number(within 1-20): ')
number = random.randint(1, 20)
guess = int(input())
for guessesTaken in range(1, 7):  # You got a max of 7 tries.
    print('Choose your number: ')
    if guess > number:
        print('Your number is too high, try again!')
    elif guess < number:
        print('Your number is too low, try again!')
    else:
        break  # If the number is correct, the loop will break.

if guess == number:
    print('You guessed my number,', name)
else:
    print('Too bad,', name, "you didn't guess my number.")
