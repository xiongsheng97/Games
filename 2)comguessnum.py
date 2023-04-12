import random

def computer_guess(x):
    low=0
    high=x
    feedback=''
    while feedback!='c':
        guess=random.randint(low,high)
        feedback=input(f'Is {guess} too high(h), or too low(l) or correct(c): ')
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
        else:
            print(f'please check the input {feedback} again:')

    print(f'the correct number is {guess}!')

computer_guess(100)