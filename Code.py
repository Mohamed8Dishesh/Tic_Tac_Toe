
print("Welcome! You are now in a game of tic-tac-toe.")
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def make_move(board, player):
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if board[row][col] == "":
            board[row][col] = player
            break
        else:
            print("That spot is already taken. Please Try again.")

def check_win(board, player):
    # Check rows
    for row in board:
        if all(square == player for square in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if (board[0][0] == board[1][1] == board[2][2] == player) or \
       (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    
    return False

def check_tie(board):
    for row in board:
        if "" in row:
            return False
    return True

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

current_player = "X"
while True:
    print_board(board)
    print("Player", current_player)
    make_move(board, current_player)
    
    if check_win(board, current_player):
        print_board(board)
        print("Player", current_player, "wins!")
        break
    elif check_tie(board):
        print_board(board)
        print("It's a tie!")
        break
    
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"