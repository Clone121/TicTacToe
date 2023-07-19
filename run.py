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
    
    # Check for winner
    def has_winner():
        # Check rows
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

main()
    
