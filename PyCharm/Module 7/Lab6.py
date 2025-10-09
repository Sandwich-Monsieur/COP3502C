def initialize_board(num_rows, num_cols):
    board = []
    for i in range(num_rows):
        board.append(["-"]*num_cols)
    return board

def print_board(board):
    for i in range(height-1, -1, -1):
        for j in range(length):
            print(board[i][j], end = " ")
        print()
    print()

def insert_chip(board, col, chip_type):
    for r in range(height):
        if board[r][col] == "-":
            board[r][col] = chip_type
            return r

def check_if_winner(board, col, row, chip_type):
    rows = len(board)
    cols = len(board[0])
    count = 0
    for r in range(rows):
        if board[r][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    count = 0
    for c in range(cols):
        if board[row][c] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

if __name__ == "__main__":
    height =  int(input("What would you like the height of the board to be? "))
    length =  int(input("What would you like the length of the board to be? "))
    
    board = initialize_board(height, length)
    print_board(board)
    
    print("Player 1: x")
    print("Player 2: o")
    print()
    turn = 0
    total_spaces = height * length
    game = True
    while game:
        if turn % 2 == 0:
            player = 1
            chip_type = "x"
        else:
            player = 2
            chip_type = "o"
        
        play = int(input(f"Player {player}: Which column would you like to choose? "))
        row = insert_chip(board, play, chip_type)
        print_board(board)
        win = check_if_winner(board, play, row, chip_type)
        if win == True:
            print(f"Player {player} won the game!")
            game = False
        turn += 1
        if turn == total_spaces:
            print("Draw. Nobody wins.")
            game = False