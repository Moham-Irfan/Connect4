# Connect4

## Description
This project implements a simple text-based version of the **Connect4** game using Python. Connect4 is a two-player game where players take turns dropping tokens into a 6x6 grid. The goal is to align four tokens of your color in a row, column, or diagonal to win the game.

---

## Game Rules
1. The game board is a 6x6 grid, displayed dynamically using the `prettytable` library.
2. Players alternate turns to drop their tokens into a column of their choice.
3. Tokens fall to the lowest available row in the selected column.
4. Each player is represented by a unique token:
   - **🔴** for Player 1
   - **🔵** for Player 2
5. Empty cells on the board are represented by `--`.
6. A player wins by connecting four of their tokens in a row, column, or diagonal.
7. If the grid is completely filled and no player has aligned four tokens, the game ends in a draw.

---

## Installation
To play the game, ensure you have Python installed on your system. Follow these steps to set up the game:

1. Clone or download the project files.
2. Install the required dependency:
   ```bash
   pip install -r requirements. txt
   ```

---

## How to Play
1. Run the program using Python:
   ```bash
   python connect4.py
   ```
2. Players will take turns selecting a column number (1-6) to drop their tokens.
3. The game will display the updated grid after each turn, with tokens and empty cells color-coded:
   - **🔴**: Player 1's token
   - **🔵**: Player 2's token
   - **--** : Empty cell
4. The game ends when:
   - A player aligns four tokens horizontally, vertically, or diagonally.
   - The grid is full, resulting in a draw.
5. At the end of the game, players can choose to replay or quit.

---

## Note :
- The game clears the console after every turn using `os.system('cls')` for Windows. If you're using a Unix-based system, replace it with `os.system('clear')` in the code.

---

## Enjoy the Game!

