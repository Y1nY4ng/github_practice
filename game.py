def print_board(board):
    """Prints the Tic Tac Toe board."""
    print("\n".join([
        " | ".join(board[i*3:(i+1)*3])
        for i in range(3)
    ]))
    print()

def check_winner(board, player):
    """Checks if the given player has won."""
    win_conditions = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal \
        [2, 4, 6]   # Diagonal /
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all(cell != ' ' for cell in board)

def main():
    board = [' '] * 9
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn")

        while True:
            try:
                move = int(input(f"Choose a position (1-9): ")) - 1
                if move < 0 or move > 8:
                    raise ValueError("Invalid position")
                if board[move] != ' ':
                    raise ValueError("Position already taken")
                break
            except ValueError as e:
                print(e)

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        turn += 1

if __name__ == "__main__":
    main()