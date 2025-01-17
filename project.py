import itertools
import sys
import os
import copy
from prettytable import PrettyTable

# currentPlayer = 1
COLUMNS = 6
ROWS = 6
MATCH = 4
box = [[0 for j in range(COLUMNS)] for i in range(ROWS)]
player = itertools.cycle([2, 1])


# box[row][column]   ..., remember this imp imp


def main():
    global box
    playAgain = True
    while playAgain:
        isEnd = False
        currentPlayer = 1
        while not isEnd:
            os.system('cls')
            # print()
            printTable()
            # print(tabulate(box, tablefmt="simple_grid"))
            makeMove(currentPlayer)
            if checkWinner(currentPlayer):
                printTable()
               # print(tabulate(box, tablefmt="simple_grid"))
                print(f"Player {currentPlayer} Won!!")
                isEnd = True
            elif checkDraw():
                printTable()
                # print(tabulate(box, tablefmt="simple_grid"))
                print("The Game is Draw")
                isEnd = True
            currentPlayer = next(player)
        box = [[0 for j in range(COLUMNS)] for i in range(ROWS)]
        # Ask whether the player wants to play again after a game ends
        ans = input("Do you want to play again? [y/n]: ").lower()
        if ans == 'y':
            playAgain = True
            currentPlayer = next(player)
        elif ans == 'n':
            sys.exit("Thank you for playing")
        else:
            sys.exit("Hmm, seems you are confused. K bye, cya later!")

        # Clear the screen before starting a new game
        os.system('cls')


def makeMove(currentPlayer):
    while True:
        rePrompt = False
        move = input(f"Player {currentPlayer}'s Turn\nChoose The Column you want to play in: ")
        # print(move)
        if not move.isnumeric():
            print("Only Integer Values Allowed")
            rePrompt = True
        elif not (int(move) in range(1, COLUMNS + 1)):
            print(f"Enter a Value between 1 and {COLUMNS}")
            rePrompt = True
        else:
            move = int(move)
            for i in range(ROWS):
                pick = box[ROWS - 1 - i][move - 1]
                if pick == 0:
                    box[ROWS - 1 - i][move - 1] = currentPlayer
                    break
            else:
                print("Invalid Turn\nThe column you picked is already full")
                rePrompt = True
        if not rePrompt:
            break


def checkHorizontal(check_board):
    for b in check_board:
        for i in range(COLUMNS - MATCH + 1):
            checkmatch = b[i:i + MATCH]
            if len(checkmatch) == MATCH and len(set(checkmatch)) == 1 and 0 not in set(checkmatch):
                return True
    return False


def checkVertical():
    transpose = [[i[j] for i in box] for j in range(COLUMNS)]
    return checkHorizontal(transpose)


def checkSlanting():
    for i in range(ROWS - MATCH + 1):
        for j in range(COLUMNS):

            # checking for Backslash or back Diagonal (\)
            if j < COLUMNS - MATCH + 1:
                bwd = [box[i + k][j + k] for k in range(MATCH)]
                if len(bwd) == MATCH and len(set(bwd)) == 1 and 0 not in set(bwd):
                    return True

            # checking for ForwardSlash (/)
            if j >= MATCH - 1:
                fwd = [box[i + l][j - l] for l in range(MATCH)]
                if len(fwd) == MATCH and len(set(fwd)) == 1 and 0 not in set(fwd):
                    return True
    return False


def checkWinner(currentPlayer):
    return checkHorizontal(box) or checkVertical() or checkSlanting()


def printTable():
    new = copy.deepcopy(box)
    for i in range(ROWS):
        for j in range(COLUMNS):
            if box[i][j] == '1' or box[i][j] == 1:
                new[i][j] = '🔴'
            elif box[i][j] == '2' or box[i][j] == 2:
                new[i][j] = '🔵'
            else:
                new[i][j] = '--'


    table = PrettyTable()
    table.add_rows(new)
    table.border = True  # Border around the table
    table.header = False  # Disable header
    table.align = "c"  # Center-align the text in columns
    table.hrules = 1  # Horizontal rules (lines) between rows

    # Print the table
    print(table)

def checkDraw():
    for row in box:
        if 0 in row:
            return False
    return True


if __name__ == '__main__':
    main()

##🔴🟦⚪
