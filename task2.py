import numpy as np

# Constants to represent the players and empty spots on the board
PLAYER_X = 1
PLAYER_O = -1
EMPTY = 0

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(["X" if cell == PLAYER_X else "O" if cell == PLAYER_O else " " for cell in row]))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i, :] == player) or all(board[:, i] == player):
            return True
    if all(np.diag(board) == player) or all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return np.all(board != EMPTY)

# Minimax algorithm to find the best move
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, PLAYER_X):
        return -10 + depth
    elif check_win(board, PLAYER_O):
        return 10 - depth
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i, j] == EMPTY:
                    board[i, j] = PLAYER_O
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i, j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i, j] == EMPTY:
                    board[i, j] = PLAYER_X
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i, j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to get the best move for the AI using minimax
def get_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i, j] == EMPTY:
                board[i, j] = PLAYER_O
                move_eval = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i, j] = EMPTY
                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = (i, j)
    return best_move

# Main game loop
def play_game():
    board = np.zeros((3, 3), dtype=int)

    while not is_board_full(board):
        print_board(board)

        # Human player's move
        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row, col] == EMPTY:
                board[row, col] = PLAYER_X
                break
            else:
                print("Cell already taken. Try again.")

        if check_win(board, PLAYER_X):
            print_board(board)
            print("You win!")
            return

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            return

        # AI player's move
        print("AI's turn:")
        best_move = get_best_move(board)
        board[best_move] = PLAYER_O

        if check_win(board, PLAYER_O):
            print_board(board)
            print("AI wins!")
            return

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            return

# Start the game
play_game()
