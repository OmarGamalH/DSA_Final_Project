import tkinter as tk
from ttkbootstrap import Style
from tkinter import simpledialog
from board import Board
from player import Player
from playsound import playsound
import os
import sqlite3 as sql
import random
from datetime import datetime

# Game configuration
ROWS, COLS = 7, 7
CELL_SIZE = 80
PADDING = 10
RADIUS = CELL_SIZE // 2 - 5
music_path = "./victory_sound/victory_sound.mp3"
music_played = False

# Game initialization
board = Board()
current_player = 1
hover_circle = None
win_text_id = None
# Database configurations
start_date = None
end_date = None
current_path = os.getcwd()
data_path_name = "dashboard.db"
full_path_db = os.path.join(current_path , data_path_name)
con = sql.connect(full_path_db)
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS game  ( 
               game_id INTEGER PRIMARY KEY AUTOINCREMENT,
               "winner name" VARCHAR(255),
               "winner number" INTEGER,
               "winner color" VARCHAR(255),
               startdate VARCHAR(255),
               enddate VARCHAR(255)
               )""")
# Solver
class solver:
    name = "solver"
    number = 2
    color = "yellow"
    solved = False

    def solve(self):

        global board
        for c in range(COLS):
            col = board.columns[c]
            if col.top != None and col.top.value == self.number and not col.is_full():
                board.drop_piece(c, current_player.number)
                draw_board()
                self.solved = True
                break

        if not self.solved:
            number = random.randint(0, COLS - 1)
            while board.columns[number].is_full():
                number = random.randint(0, COLS - 1)
            board.drop_piece(number, current_player.number)
            draw_board()
        self.solved = False


# GUI
root = tk.Tk()
root.title("Connect 4 - Player Turns")

# dark theme
style = Style("darkly")
root.configure(bg="#1e3d59")

player1 = None
player2 = None
current_player = None

# Setting dimensions
canvas_width = COLS * CELL_SIZE
canvas_height = (ROWS + 1) * CELL_SIZE
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="#1e3d59", highlightthickness=0)

canvas.pack(padx=20, pady=20)

# displaying player turn
player_label = tk.Label(root, text=f"Player {current_player}'s Turn", font=("Arial", 16), bg="#1f1f2e", fg="white")
player_label.pack(pady=(0, 10))
error_label = tk.Label(root, text="", font=("Arial", 14), fg="red", bg="#1f1f2e")
error_label.pack()


# game board
def draw_board():
    canvas.delete("board")
    canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="#1e3d59", width=0, tags="board")

    for r in range(ROWS):
        for c in range(COLS):
            x0 = c * CELL_SIZE + PADDING
            y0 = (r + 1) * CELL_SIZE + PADDING
            x1 = x0 + CELL_SIZE - 2 * PADDING
            y1 = y0 + CELL_SIZE - 2 * PADDING

            # Get cell value to determine color
            value = board.board[ROWS - 1 - r][c]
            if value == 0:
                color = "white"  # empty
            elif value == player1.number:
                color = player1.color
            else:
                color = player2.color

            canvas.create_oval(x0, y0, x1, y1, fill=color, outline="gray", tags="board")


# player names
def ask_player_names():
    global player1, player2, current_player

    dialog = tk.Toplevel(root)
    dialog.title("Choose Game Mode")
    dialog.configure(bg="#1f1f2e")
    dialog.geometry("350x300")
    dialog.resizable(False, False)

    dialog.transient(root)
    dialog.grab_set()
    dialog.attributes('-topmost', True)

    tk.Label(dialog, text="Select Game Mode", font=("Arial", 14, "bold"), bg="#1f1f2e", fg="white").pack(pady=(10, 5))

    mode_var = tk.StringVar(value="2")  # default to 2 players

    # Radio buttons for game mode
    tk.Radiobutton(dialog, text="1 Player (vs Computer)", variable=mode_var, value="1", bg="#1f1f2e", fg="white",
                   selectcolor="#1e3d59").pack(pady=(5, 2))
    tk.Radiobutton(dialog, text="2 Players", variable=mode_var, value="2", bg="#1f1f2e", fg="white",
                   selectcolor="#1e3d59").pack(pady=(2, 10))

    # Player 1 name input
    tk.Label(dialog, text="Player 1 (Red):", bg="#1f1f2e", fg="white").pack()
    p1_entry = tk.Entry(dialog)
    p1_entry.pack(pady=(0, 10))

    # Player 2 name input (conditionally shown)
    p2_label = tk.Label(dialog, text="Player 2 (Yellow):", bg="#1f1f2e", fg="white")
    p2_entry = tk.Entry(dialog)

    def update_visibility(*args):
        if mode_var.get() == "2":
            p2_label.pack()
            p2_entry.pack()
        else:
            p2_label.pack_forget()
            p2_entry.pack_forget()

    mode_var.trace("w", update_visibility)
    update_visibility()

    # Create Player objects
    def create_players(name1, name2=None):
        global player1, player2, current_player , start_date
        start_date = datetime.now()
        player1 = Player(1, name1, "red")
        if mode_var.get() == "1":
            player2 = solver()
        else:
            player2 = Player(2, name2, "yellow")
        current_player = player1
        player_label.config(text=f"{current_player.name}'s Turn", bg=current_player.color, fg="blue")

    # Handle Start button
    def on_start():
        name1 = p1_entry.get().strip() or "Player 1"
        name2 = p2_entry.get().strip() or "Player 2"
        dialog.destroy()
        create_players(name1, name2)

    tk.Button(dialog, text="Start Game", command=on_start).pack(pady=20)
    dialog.wait_window(dialog)



def update_hover(event):
    if not (current_player == player2 and player2.name == "solver"):
        global hover_circle
        canvas.delete("hover")

        col = event.x // CELL_SIZE
        if col < 0 or col >= COLS:
            return

        x0 = col * CELL_SIZE + PADDING
        y0 = PADDING
        x1 = x0 + CELL_SIZE - 2 * PADDING
        y1 = y0 + CELL_SIZE - 2 * PADDING

        canvas.create_oval(x0, y0, x1, y1, fill="#1e3d59", outline="", tags="hover")

        hover_circle = canvas.create_oval(x0, y0, x1, y1, fill=current_player.color, outline="white", width=2,
                                          tags="hover")


# Handle click to drop a piece
def handle_click(event):
    global current_player, win_text_id
    if not (current_player == player2 and player2.name == "solver"):
        col = event.x // CELL_SIZE
        if col < 0 or col >= COLS:
            return

        # If column is full
        if not board.is_valid_location(col):
            error_label.config(text=" Column is full, choose another column.", bg="#1e3d59")
            return
        else:
            error_label.config(text="")

        # Drop the piece and update board
        board.drop_piece(col, current_player.number)
        draw_board()
        canvas.delete("hover")

    # Check for win
    if board.check_win(current_player.number):
        canvas.unbind("<Button-1>")
        canvas.unbind("<Motion>")
        canvas.delete("board")
        canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="#1e3d59", width=0)

        player_label.config(text="")

        # Show win message
        win_text_id = canvas.create_text(
            canvas_width // 2,
            canvas_height // 2 - 30,
            text=f" {current_player.name} Wins!",
            font=("Arial", 48, "bold"),
            fill="white"
        )
        cursor.execute("INSERT INTO game('winner name' , 'winner number' , 'winner color' , startdate , enddate) VALUES(? , ? , ? ,  ? , ?)" , (current_player.name , current_player.number , current_player.color , start_date , datetime.now()) )
        con.commit()
        global music_played
        if os.path.exists(music_path) and not music_played:
            music_played = True
            playsound(music_path)
        return

    # Check for draw
    if board.is_full():
        player_label.config(text="It's a draw!")
        return

    # Switch to next player
    current_player = player2 if current_player == player1 else player1
    if current_player == player2 and player2.name == "solver":
        player2.solve()
        handle_click(event)
    player_label.config(text=f"{current_player.name}'s Turn", bg=current_player.color, fg="blue")


# Reset the game
def reset_game():
    global current_player, win_text_id
    ask_player_names()
    board.reset()
    draw_board()
    canvas.bind("<Button-1>", handle_click)
    canvas.bind("<Motion>", update_hover)
    player_label.config(text=f"{current_player.name}'s Turn", bg=current_player.color, fg="blue")
    global music_played
    music_played = False

    if win_text_id:
        canvas.delete(win_text_id)
        win_text_id = None

def undo_last_move():
    global current_player, win_text_id, music_played

    if current_player.name == "solver":
        return

    board.undo_move()
    current_player = player2 if current_player == player1 else player1
    draw_board()
    canvas.bind("<Button-1>", handle_click)
    canvas.bind("<Motion>", update_hover)
    player_label.config(text=f"{current_player.name}'s Turn", bg=current_player.color, fg="blue")

    if win_text_id:
        canvas.delete(win_text_id)
        win_text_id = None

    music_played = False
    error_label.config(text="")



button_frame = tk.Frame(root)
button_frame.pack(pady=(0, 10))


undo_btn = tk.Button(button_frame, text="Undo", command=undo_last_move,
                     font=("Arial", 25, "bold"), width=9, height=1)
undo_btn.pack(side="left", padx=5)

#Reset
reset_btn = tk.Button(button_frame, text="Reset", command=reset_game,
                      font=("Arial", 25, "bold"), width=9, height=1)
reset_btn.pack(side="left", padx=5)

# mouse events
canvas.bind("<Motion>", update_hover)
canvas.bind("<Button-1>", handle_click)

# Initialization board and game
draw_board()
ask_player_names()
player_label.config(text=f"{current_player.name}'s Turn", bg=current_player.color, fg="blue")

# Starting the main
root.mainloop()
cursor.close()
