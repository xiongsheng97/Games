import random

def guess(x):
    randomnum=random.randint(1,x)
    guess=0
    while guess!=randomnum:
        guess=int(input(f'Guess a number betweem 1 and {x}:'))
        if guess <randomnum:
            print('sorry, guess again. your input {guess} is too low')
        elif guess>randomnum:
            print('sorry, guess again. your input {guess} is too high')

    print(f'congrats! your guess {guess} is correct')

guess(100)