import numpy as np
import sys
from columnstack import ColumnStack

class Board:
    def __init__(self):
        self.rows = 7
        self.cols = 7
        self.board = np.zeros((self.rows, self.cols), dtype=int)
        self.columns = [ColumnStack() for _ in range(self.cols)]
        # for undo
        self.move_history = []

    def display(self):
        print("\nCurrent Board:")
        print(np.flip(self.board, 0))

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
                if all(b[r][c + i] == player for i in range(4)):
                    return True

        # Vertical
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if all(b[r + i][c] == player for i in range(4)):
                    return True

        # Positive diagonal (/)
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if all(b[r - i][c + i] == player for i in range(4)):
                    return True

        # Negative diagonal (\)
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if all(b[r + i][c + i] == player for i in range(4)):
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
                    print("Invalid column. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Enter a number from 0 to 6.")
                continue

            if not board.is_valid_location(col):
                print("This column is full. Try another one.")
                continue

            board.drop_piece(col, player)
            board.display()

            if board.check_win(player):
                print(f"\nPlayer {player} WINS")
                game_over = True
                break

            if board.is_full():
                print("\n It's a draw. The board is full.")
                break

            turn += 1

            """
            if turn == 5:
                board.undo_move()
            if turn == 6:
                board.reset()
            """
        print("Game over.")



# Run the game
if __name__ == "__main__":
    Board.play_game()
