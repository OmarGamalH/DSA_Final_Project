import columnstack
import numpy as np
import sys

from columnstack import ColumnStack





class ColumnStack:
    def __init__(self):
        self.stack = []

    @property
    def length(self):
        return len(self.stack)

    def push_piece(self, value):
        if self.length < 7:
            self.stack.append(value)
        else:
            raise Exception("Column is full")

    def get_stack(self):
        return self.stack

    def push_piece(self, value):
        if len(self.stack) < 7:
            self.stack.append(value)
        else:
            raise ValueError("Column is full")

    def pop_piece(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_full(self):
        return len(self.stack) >= 7







class Board:
def __init__(self):
self.rows=7
self.cols=7
self.board =np.zeros ((self.rows,self.cols),dtype=int)
self.columns =[ColumnStack () for_in range(self.cols)]
#for undoo
self.move_history = []



def display (self):
print ("\Current Board :")
print (np.flip(self.Board ,0))


 def is_valid_location(self, col):
     return not self.columns[col].is_full()


 def drop_piece(self, col, player):
        if not self.is_valid_location(col):
            raise ValueError("Column is full")
        row = self.columns[col].length
        self.columns[col].push_piece(player)
        self.board[row][col] = player
        self.move_history.append((row, col))
        return row
     
  def is_full(self):
     return all(col.is_full() for col in self.columns)



  def reset(self):
     self.board = np.zeros((self.rows, self.cols), dtype=int)
    self.columns = [ColumnStack() for _ in range(self.cols)]
    self.move_history.clear()

   def undo_move(self):
        if not self.move_history:
            return
        row, col = self.move_history.pop()
        self.columns[col].pop_piece()
        self.board[row][col] = 0



    def check_win(self, player):
        b = self.board

        # Horizontal
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if all(b[r][c+i] == player for i in range(4)):
                    return True

        # Vertical
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if all(b[r+i][c] == player for i in range(4)):
                    return True

        # Positive diagonal (/)
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if all(b[r-i][c+i] == player for i in range(4)):
                    return True

        # Negative diagonal (\)
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if all(b[r+i][c+i] == player for i in range(4)):
                    return True

        return False
def play_game():
    board = Board()
    game_over = False
    turn = 0

    board.display()

    while not game_over:
        player = 1 if turn % 2 == 0 else 2
        print(f"\nPlayer {player}'s turn")

        try:
            col = int(input("Choose a column (0–6): "))
            if col < 0 or col >= board.cols:
                print(" Invalid column. Try again.")
                continue
        except ValueError:
            print(" Invalid input. Enter a number from 0 to 6.")
            continue

        if not board.is_valid_location(col):
            print(" This column is full. Try another one.")
            continue


        board.drop_piece(col, player)
        board.display()

        if board.check_win(player):
            print(f"\n Player {player} WINS ")
            game_over = True
            break


        if board.is_full():
            print("\n🟰 It's a draw The board is full.")
            break

        turn += 1

    print("Game over.")

# Run the game
if __name__ == "__main__":
    play_game()






###########mona 
"""
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
    else:
        print("This column is full. Try again.")
        Player_turn -= 1  
        continue
"""
