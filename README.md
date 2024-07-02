# TicTacToegame
This is a simple Tic-Tac-Toe game implemented in Python. The game is played in the console, allowing two players to take turns marking the cells in a 3×3 grid with `X` and `O`.

Gameplay Instructions:

1.The game begins with a welcome message: "Welcome to Tic Tac Toe Game by Isha".

2.Players take turns to enter their move in the format row,column (e.g., 1,1 for the top-left cell).

3.The board will be displayed after each move.


4.The game checks for a winner after each move and announces the winner if there is one.

5.If the board is full and there is no winner, the game declares a draw.

6.The game ends with the message "Better luck next time" if no winner is found.

Features:

1.User-Friendly Input: Players enter their moves using a simple row and column format.

2.Input Validation: The game checks for valid moves and prompts the player to try again if the input is invalid or the cell is already taken.

3.Win and Draw Detection: The game accurately detects win conditions and draws.

4.Console Output: The current state of the board is displayed after each move.

Code Explanation:
1.print_board(board): Prints the current state of the game board.

2.check_winner(board, player): Checks if the specified player has won the game.

3.is_draw(board): Checks if the game is a draw.

4.get_move(): Prompts the player to enter their move and validates the input.

5.main(): Main game loop that handles player turns, board updates, and win/draw conditions.
