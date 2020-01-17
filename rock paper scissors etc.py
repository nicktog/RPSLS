# Rock Paper Scissors Lizard Spock by Nick Togneri

import random
import math

def player_move():
    move = input("Player chooses ")
    return move

def rand():
    comp_move=random.randrange(0,4)
    return comp_move

def name_to_number(x):
    if x == 'rock':
        move = 0
    elif x == 'spock':
        move = 1
    elif x == 'paper':
        move = 2
    elif x == 'lizard':
        move = 3
    elif x == 'scissors':
        move = 4
    else:
        print ('Not a valid move')
        move = None
    return move
 
def number_to_name(y):
    if y == 0:
        name = 'rock'
    elif y == 1:
        name = 'spock'
    elif y == 2:
        name = 'paper'
    elif y == 3:
        name = 'lizard'
    elif y == 4:
        name = 'scissors'
    else:
        print ('Hmmmmm, not a valid number')
        name = None
    return name

def winner(move, comp_move):
    print move, comp_move
    print ((move - comp_move) % 5)
    if move == comp_move:
        winner = 'Player and Computer tie!'
    elif (move - comp_move) % 5 > 2:
        winner = "Computer wins!"
    elif (move - comp_move) % 5 <= 2:
        winner = "Player wins!"
    else:
        print 'hmmmm' 
    return winner

def yorn():
    play = input('Again (y or n)?')
    return play

while True:   
    move = player_move()
    comp_move = rand()
    this = name_to_number(move)
    final = winner (this, comp_move)
    print 'Player plays', move
    print 'Computer plays', number_to_name(comp_move)
    print (final)
    print 
    if yorn() == 'y': continue
    else:
        print 'Bye!'
        break