import tkinter as tk
from ttkbootstrap import Style
from tkinter import simpledialog
from board import Board
from player import Player

# Game configuration
ROWS, COLS = 7, 7
CELL_SIZE = 80
PADDING = 10
RADIUS = CELL_SIZE // 2 - 5

# Game initialization
board = Board()
current_player = 1
hover_circle = None
win_text_id = None

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

#displaying player turn
player_label = tk.Label(root, text=f"Player {current_player}'s Turn", font=("Arial", 16), bg="#1f1f2e", fg="white")
player_label.pack(pady=(0, 10))
error_label = tk.Label(root, text="", font=("Arial", 14), fg="red", bg="#1f1f2e")
error_label.pack()

#game board
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
                color = "white" #empty
            elif value == player1.number:
                color = player1.color
            else:
                color = player2.color

            canvas.create_oval(x0, y0, x1, y1, fill=color, outline="gray", tags="board")

# player names
def ask_player_names():
    global player1, player2, current_player

    dialog = tk.Toplevel(root)
    dialog.title("Enter Player Names")
    dialog.configure(bg="#1f1f2e")
    dialog.geometry("300x200")
    dialog.resizable(False, False)

    dialog.transient(root)
    dialog.grab_set()
    dialog.attributes('-topmost', True)

    # Entry for Player 1
    tk.Label(dialog, text="Player 1 (Red):", bg="#1f1f2e", fg="white").pack(pady=(20, 5))
    p1_entry = tk.Entry(dialog)
    p1_entry.pack()

    # Entry for Player 2
    tk.Label(dialog, text="Player 2 (Yellow):", bg="#1f1f2e", fg="white").pack(pady=(10, 5))
    p2_entry = tk.Entry(dialog)
    p2_entry.pack()

    # Create Player objects
    def create_players(name1, name2):
        global player1, player2, current_player
        player1 = Player(1, name1, "red")
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


    hover_circle = canvas.create_oval(x0, y0, x1, y1, fill=current_player.color, outline="white", width=2, tags="hover")

# Handle click to drop a piece
def handle_click(event):
    global current_player, win_text_id

    col = event.x // CELL_SIZE
    if col < 0 or col >= COLS:
        return

    # If column is full
    if not board.is_valid_location(col):
        error_label.config(text="⚠️ Column is full, choose another column.",bg="#1e3d59")
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
            text=f"🎉 {current_player.name} Wins!",
            font=("Arial", 48, "bold"),
            fill="white"
        )
        return

    # Check for draw
    if board.is_full():
        player_label.config(text="It's a draw!")
        return

    # Switch to next player
    current_player = player2 if current_player == player1 else player1
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

    if win_text_id:
        canvas.delete(win_text_id)
        win_text_id = None

# Reset button
reset_btn = tk.Button(root, text="Reset", command=reset_game, font=("Arial", 25, "bold"), width=9, height=1)
reset_btn.pack(pady=(0, 10))

# mouse events
canvas.bind("<Motion>", update_hover)
canvas.bind("<Button-1>", handle_click)

# Initialization board and game
draw_board()
ask_player_names()
player_label.config(text=f"{current_player.name}'s Turn", bg=current_player.color, fg="blue")

# Starting the main
root.mainloop()
