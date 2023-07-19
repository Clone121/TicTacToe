def main():
    print("##############################")
    print("### Welcome to Tic Tac Toe ###")
    print("##############################")
    print("The rules of the game")
    print("Player X chooses a row 1-3")
    print("the a column 1-3")
    print("Then player O choose a roew and column 1-3")
    print("The game continues until there is a winner, or the game is tie")
    print("Have fun")

    board = [["-", "-", "-"],
             ["-", "-", "-",],
             ["-", "-", "-"]]

    rows = 3
    cols = 3

    # Prints out the Game board
    def print_board():
        for x in range(rows):
            print("\n+---+---+---+")
            print("|", end="")
            for y in range(cols):
                print("", board[x][y], end=" |")
        print("\n+---+---+---+")
    
    #Check for winner
    def has_winner():
        #Check rows
        if board[0][0] == board[0][1] == board[0][2] != "-":
            return True
        elif board[1][0] == board[1][1] == board[1][2] != "-":
            return True
        elif board[2][0] == board[2][1] == board[2][2] != "-":
            return True
        # Check columns
        elif board[0][0] == board[1][0] == board[2][0] != "-":
            return True
        elif board[0][1] == board[1][1] == board[2][1] != "-":
            return True
        elif board[0][2] == board[1][2] == board[2][2] != "-":
            return True
        # Check the diagonal
        elif board[0][0] == board[1][1] == board[2][2] != "-":
            return True
        elif board[0][2] == board[1][1] == board[2][0] != "-":
            return True
        else:
            return False

    # Check if the game is tied
    def game_tie():
        for row in board:
            for element in row:
                if element == "-":
                    return False
        return True
    
    # Start Game
    def play(player_turn):

        print_board()

        while True:
            print("Player " + player_turn + ", your turn")

            input_ok = False
            row = ""
            column = ""
            while not input_ok:
                row = input("Choose row ")
                if not row.isnumeric():
                    print("That's not a valid number")
                    continue
                if int(row) > 3 or int(row) < 1:
                    print("Out of bounds")
                    continue

                column = input("Choose column ")
                if not column.isnumeric():
                    print("That's not a valid number")
                    continue
                if int(column) > 3 or int(column) < 1:
                    print("Out of bounds")
                    continue
                if row in ["1", "2", "3"] and column in ["1", "2", "3"]:
                    row = int(row) -1
                column = int(column) -1
                if board[row][column] == "-":
                    input_ok = True
                else:
                    print("This position is already taken, try again")
            else:
                print("Try again.")
            board[row][column] = player_turn

            print_board()

main()
    
