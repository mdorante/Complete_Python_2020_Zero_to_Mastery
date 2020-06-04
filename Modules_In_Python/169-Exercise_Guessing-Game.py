# generate a number 1-10

# input from user, check that it's a number 1-10
# check if the number is the right guess, otherwise, ask again
# the game must have parameters passed in by terminal to determine start and end of the guessing range

from random import randint
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
number = randint(start, end)

while True:
    try:
        guess = int(input(f'Guess a number {start}-{end}:   '))
        if guess == number:
            print('Congrats, you win!')
            break
        elif guess not in range(start, (end + 1)):
            print(f'I said enter a number {start}-{end}, guess again')
        else:
            print('Guess again')
    except ValueError:
        print('Please enter a number')
