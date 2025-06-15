
# 🎮 Connect 4 - GUI Game with Python, Tkinter & ttkbootstrap

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A modern and interactive **Connect 4** game built in Python using **Tkinter** for the GUI and **ttkbootstrap** for a stylish dark theme. It features custom player names, hover effects, win detection, and a responsive user interface.

---
## 🕹️ How to Play

1. Enter custom player names when prompted.
2. Player 1 uses **Red**, Player 2 uses **Yellow**.
3. Hover over a column to preview your move.
4. Click to drop your piece in the selected column.
5. The first player to connect four wins.
6. If the board fills up, it's a draw.
7. Click **Reset** to start a new game.

---
## 📸 Preview

# Blank Board
<div align="center">
  <img src="https://github.com/user-attachments/assets/df960826-7ada-431b-b477-978336bed824" alt="Image" width="400"/>
</div>

# Game States

<div align="center">
<table>
  <tr>
    <th>Switching Turns </th> 
    <th>Winning Message</th> 
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/bceaafd5-16df-4ca5-a885-826ad2559ddc" alt="Before" width="300"/></td>
    <td><img src="https://github.com/user-attachments/assets/b768e5fd-004d-4add-ae74-fe7e8157bc06" alt="After" width="300"/></td>
  </tr>
</table>

</div>

---
## Score System
- Player scores are updated after each winning round.
- Scores are displayed on the game interface to track each player’s progress.
- The scoring system can be used to determine the overall winner after multiple rounds.

<div align="center">
  <img src="https://github.com/user-attachments/assets/f4609689-a4fc-4f95-9f8e-5911519a9fe4" alt="Image" width="400"/>
</div>
 
---
## Database
- A SQLite database is used to store game information.
- Each round’s data is saved in a dedicated table, including:
  - Winner’s name , Player number, Player color , Round start time (`startdate`) ,  Round end time (`enddate`)
- This enables later analysis, game history review, and player performance statistics.
-  Every completed round is recorded in a rounds table within the database.
- Round results are saved immediately after the round ends to ensure data integrity.
- This table can be used to retrieve past game sessions, replay rounds, or track player progress over multiple rounds.
   ![Image](https://github.com/user-attachments/assets/88d4d6fb-9733-41e3-85ba-ac434935f324)
---
## Continue Prompt
- After each round, a prompt asks players if they want to continue playing.
- If players agree, a new round starts with the board reset but scores retained.
- If players decline, the game ends and a final summary is displayed.
- This feature improves user experience by allowing seamless multiple rounds without restarting the game manually.
  <div align="center">
  <img src="https://github.com/user-attachments/assets/f6eb30b8-528e-4331-998a-5ab14e980e8b" alt="Image" width="400"/>
</div>

## 💻 Data Structures Used

- A 2-D char array has been used to build the game board which allows players to make a move.

- The *Linear Search Algorithm* is used to check for win diagonally, horizontally or vertically.

- *Stack Data Structure* used to push and pop a move that has been made by a player.

- *Array* used to save the move history.


## 🧩 Features

- ✅ 7x7 Game Grid  
- ✅ Two Player Mode with Custom Names
- ✅ Computer mode where you can play against the PC 
- ✅ Hover Preview Before Dropping Piece  
- ✅ Win Detection (Vertical, Horizontal, Diagonal)  
- ✅ Draw Detection  
- ✅ Reset Button to Restart the Game  
- ✅ Dark Theme using ttkbootstrap  
- ✅ Input Validation and User Feedback
- ✅ Dashboard being saved in database
- ✅ Undo button to undo the steps
- ✅ Winning sound at the end of each game
---

## 🤖 Solver Class – Simple AI for One-Player Mode

The Solver class represents a basic automated opponent (AI) used in **1-Player Mode** of the Connect 4 game.

### 📌 Purpose:
This class provides a **basic AI opponent** for casual solo play. It is not strategic, but adds a fun and simple challenge by reacting to its previous moves or picking randomly.

![Image](https://github.com/user-attachments/assets/bc70c54e-e531-4edd-b8ab-30474aa0e259)

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.7 or higher
- `pip` package manager

### 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/connect4-gui.git
   cd connect4-gui
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   _or manually:_
   ```bash
   pip install numpy ttkbootstrap
   ```

3. **Run the game**
   ```bash
   python game.py
   ```

---



## 🗂️ Project Structure

```
connect4-gui/
├── game.py           # Main GUI application
├── board.py          # Game logic and win checks
├── piece.py          # Stack structure for each column
├── player.py         # Player class (name, number, color)
├── requirements.txt  # List of dependencies
├── dashboard.db      # Database to save winners of each game
└── README.md         # Project documentation
```

---

## 📥 Requirements

You can install requirements.txt:

```bash
pip install -r requirements.txt
```

---

## 💡 Future Improvements


- 🌐 Convert to a web app using Flask or Django

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.  
To contribute:

1. Fork the repo  
2. Create a branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m 'Add some feature'`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## 📜 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for more info.

---

## 🙋‍♂️ contributors

1. Mona Elkhouly @MonaElkhouly
2. Rowida Mohammed @rowida117
3. Aya Emad @Aya423
4. Omar Gamal @OmarGamalH

---
