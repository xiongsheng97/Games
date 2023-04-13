import random

def play():
    user= input("'r' for rock, 'p' for paper, 's' for scissors:")
    computer=random.choice(['r','p','s'])

    if user==computer:
        return'DRAW!'
    
    if win(user,computer):
        return'You won'

    return 'You lost'

#r>s,s>p,p>r
def win(player,opp):
    if (player=='r' and opp=='s'or player=='s' and opp=='p' or player=='p' and opp=='r'):
        return True

print(play())