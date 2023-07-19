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
            print("|",end="")
            for y in range(cols):
                print("",board[x][y],end=" |")
        print("\n+---+---+---+")
    




main()
    
