import random
import numpy as np
import string
from hangman_visual import lives_visual_dict
from words import words
#filename='words.txt'
#words=np.loadtxt(filename,delimiter='"', dtype=str)

def valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word or ','in word:
        word=random.choice(words)

    return word.upper()

def hangman():
    word=valid_word(words)
    word_letters=set(word) #letters in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set() # what the user has guesses
    lives=7
    # getting user input
    while len(word_letters)>0 and lives>0:
        print('You have',lives,'lives left and you have used these letters: ',','.join(used_letters))
        wordlist=[letter if letter in used_letters else "-" for letter in word]
        print('current word:',' '.join(wordlist))
        print(lives_visual_dict[lives])

        user_letter=input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives=lives-1
                print('Letter not in word.')

        elif user_letter in used_letters:
            print('You already used the character. Please try again ')
        else:
            print('Invalid character. Try again.')
    if lives==0:
        print(lives_visual_dict[lives])
        print('You died, the word was:',word)

    else:
        print('You have guess the word',word,"!!")

    


hangman()
input('Press ENTER to exit') 
