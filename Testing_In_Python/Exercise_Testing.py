# Take the code from the Guessing Game you made before and separate it into units for testing
# create a test2 file and test it

import random

start = 1
end = 10
number = random.randint(start, end)


def run_guess(guess, number):
    if guess == number:
        print('Congrats, you win!')
        return True
    elif guess not in range(start, (end + 1)):
        print(f'I said enter a number {start}-{end}, guess again')
        return False
    else:
        print('Guess again')


if __name__ == '__main__':
    while True:
        try:
            guess = int(input('guess a number 1-10: '))
            if (run_guess(guess, number)):
                break
        except ValueError:
            print('please enter a number')
            continue
