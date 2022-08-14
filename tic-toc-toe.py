import random
#This is the board that we are going to play the game 
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

currentPlayer = "X" #This represents which player is playing

winner = None

gameRunning = True

#print the game board
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

#Take in player input
def playerInput(board):
    player_chose = int(input("Enter a number between 1 and 8: "))
    if player_chose >= 1 and player_chose <= 9 and board[player_chose - 1] == "-":
        board[player_chose - 1] = currentPlayer
    else:
        print("The number is taken")


#print the winner and look for tie
#In this we are going to check if the plyaer wins horizentalley
def check_Horizental(board):
    global winner

    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

#This will check the rows and see if anyone wins there
def check_rows(board):
    global winner

    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[0]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

#This will check for a winner diagnel. 
def check_Diagnel(board):
    global winner

    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


#This will check for Tie
def check_tie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie")
        gameRunning = False

#This will check for winner
def check_win():
    if check_Diagnel(board) or check_Horizental(board) or check_rows(board):
        print(f"The winner is {winner}")


#This will switch the player from x to o and to x
def switch_player():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


#This will alow us to play with a computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()


while gameRunning:
    printBoard(board)
    playerInput(board)
    check_win()
    check_tie(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)