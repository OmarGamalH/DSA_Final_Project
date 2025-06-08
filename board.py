import columnstack
import numpy as np
import sys

from columnstack import ColumnStack


def create_board():
    board = np.zeros((7,7))
    return board
def vaild_location(board,position):
    return board[6][position] == 0
board =  create_board()
columns =[ColumnStack() for _ in range(7)]
start_game = True
Player_turn = 0

while start_game:
    print(board)
    if (Player_turn % 2) == 0:
        print("Player 1 turn ")
        position = int(input("player 1 choose a column from 0 to 6:"))
        value = 1
        Player_turn +=1

    else:
        print("Player 2 turn ")
        position = int(input("player 2 choose a column from 0 to 6:"))
        value = 2
        Player_turn += 1

    if position < 0 or position >= 7:
        print("Invalid column Try again.")
        continue

    if columns[position].length < 7:
        columns[position].push_piece(value)
        row = (columns[position].length - 1)
        board[row][position]= value