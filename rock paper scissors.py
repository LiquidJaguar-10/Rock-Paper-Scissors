import random

a = input('Enter your name whoever you are:')
print('Welcome to my arena:', a)

inputs = ["rock", "paper","scissors"]
bot = random.choice(inputs)
player = None

while player not in inputs:
    player = input('rock, paper or scissors?').lower()
    if player not in inputs:
        print('Enter a valid choice')

if player == bot:
    print('Player\'s choice:', player)
    print('Bot\'s choice:', bot)
    print('Scores are level!')
elif player == 'paper':
    if bot == 'scissors':
        print('Player\'s choice:',player)
        print('Bot\'s choice:',bot)
        print('You lost haha get good!')
    if bot == 'rock':
        print('Player\'s choice:',player)
        print('Bot\'s choice:', bot)
        print('You Won the game!!! Now say SIUUUU')
elif player == 'rock':
    if bot == 'scissors':
        print('Player\'s choice:',player)
        print('Bot\'s choice:',bot)
        print('You Won the game!!! Now say SIUUUU')
    if bot == 'paper':
        print('Player\'s choice:',player)
        print('Bot\'s choice:', bot)
        print('You lost haha get good!')
elif player == 'scissors':
    if bot == 'rock':
        print('Player\'s choice:',player)
        print('Bot\'s choice:',bot)
        print('You lost haha get good!')
    if bot == 'paper':
        print('Player\'s choice:',player)
        print('Bot\'s choice:', bot)
        print('You Won the game!!! Now say SIUUUU')
