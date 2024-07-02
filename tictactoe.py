# Tic-Tac-Toe Game by Isha

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_move():
    while True:
        move = input("Enter your move as row,col (e.g., 1,1): ")
        try:
            rowsfortictac, columnsfortictac = map(int, move.split(','))
            if rowsfortictac in range(1, 4) and columnsfortictac in range(1, 4):
                return rowsfortictac - 1, columnsfortictac - 1
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter in the format row,col.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe Game by Isha")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn")
        rowsfortictac, columnsfortictac = get_move()
        
        if board[rowsfortictac][columnsfortictac] == " ":
            board[rowsfortictac][columnsfortictac] = current_player
        else:
            print("Cell already taken. Try again.")
            continue
        
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"
    
    print("Better luck next time")

if __name__ == "__main__":
    main()
