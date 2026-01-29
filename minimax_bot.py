import tkinter as tk
from tkinter import messagebox

# Tic-Tac-Toe board (3x3 grid)
board = [' ' for _ in range(9)]
current_player = "X"  # The player always starts first

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]  # Diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the board is full (draw)
def is_board_full(board):
    return ' ' not in board

# Minimax algorithm
def minimax(board, is_maximizing):
    if check_winner(board, 'X'):
        return -1  # Opponent wins
    elif check_winner(board, 'O'):
        return +1  # AI wins
    elif is_board_full(board):
        return 0  # Draw

    if is_maximizing:  # AI's turn (maximizing player)
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # AI makes a move
                score = minimax(board, False)
                board[i] = ' '  # Undo the move
                best_score = max(best_score, score)
        return best_score
    else:  # Opponent's turn (minimizing player)
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # Opponent makes a move
                score = minimax(board, True)
                board[i] = ' '  # Undo the move
                best_score = min(best_score, score)
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    best_move = None
    best_score = -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'  # AI makes a move
            score = minimax(board, False)
            board[i] = ' '  # Undo the move
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Function to handle the player's move
def player_move(index):
    global current_player
    if board[index] == ' ' and current_player == 'X':
        board[index] = 'X'
        buttons[index].config(text="X")
        if check_winner(board, 'X'):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            reset_game()
        elif is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_game()
        else:
            current_player = "O"
            ai_move()

# Function for AI's move
def ai_move():
    global current_player
    index = find_best_move(board)
    board[index] = 'O'
    buttons[index].config(text="O")
    if check_winner(board, 'O'):
        messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
        reset_game()
    elif is_board_full(board):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        reset_game()
    else:
        current_player = "X"

# Reset the game
def reset_game():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ")

# GUI setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=('normal', 40, 'normal'), width=5, height=2,
                       command=lambda i=i: player_move(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the GUI event loop
root.mainloop()
