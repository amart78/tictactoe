from re import X
from array import *
 
a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'
h = 'h'
i = 'i'
 
# 2D arrary to represent tictactoe game board
ttt_board = [
            [a, b, c],
            [d ,e ,f],
            [g, h, i]
                    ]
 
# Find dimension/size of board (traditionally 3x3 but added to accommodate other sizes)
board_size = len(ttt_board[0])
# print(board_size)
 
# Identify row 'coordinates'
x = 0
y = 0
 
while x < board_size:
    while y < board_size :
        # print(x, y)
        y+=1
    y = 0
    x+= 1
 
# Identify column 'coordinates'
x = 0
y = 0
 
while y < board_size:
    while x < board_size:
        # print(x, y)
        x+=1
    x = 0
    y+= 1
 
x = 0
y = 0
 
# Identify L to R diagonal 'coordinates'
while x < board_size:
    while y < board_size:
        # print(x, y)
        x+= 1
        y+= 1
 
# Identify R to L diagonal 'coordinates'
x = 0
y = 2
 
while x < board_size:
    while y >= 0:
        # print(x, y)
        x+= 1
        y-= 1

  
def game():
    # Game intro & starting board presentation
    print("Let's play tic tac toe! Each position on the board is represented by a letter.")
    print("Please review the game board below & choose your position accordingly. Player X is first!")
    
    for row in ttt_board:
        for val in row:
            print(val, end=" ")
        print()

# default starting player is X
    player = 'X'
    
# while there are open positions, continue game
    not_all_x_o = True

    while not_all_x_o:

    # player picks the letter associated with the spot they'd like to choose
        position = input(f"Player {player}, choose your position: ")
    
        if position == 'O' or position == 'X' or position == None:
            print('Invalid option inputted. Try again.')
        else:
    # index/coordinates of the chosen letter are found
            for i, j in enumerate(ttt_board):
                if position in j:
                    index = (i,j.index(position))
                    break
            print(f"{position} is located at {index}")

        # update board accordingly using the coordinates of the letter found above
            ttt_board[index[0]][index[1]] = player

        # view updated game board
            for row in ttt_board:
                for val in row:
                    print(val, end = " ")
                print()

        # check game status
            not_all_x_o = False
            winning_combo = False

            for list in ttt_board:
                for val in list:
                    if val != 'X' and val != 'O':
                        not_all_x_o = True
                
            if not_all_x_o == False:
                print("Tie game! Play again.")

        # switching players
            if player == "X":
                player = "O"
            else:
                player = "X"
 
# else (if winning combo IS present), the last player who did their turn wins. Reset game
 
game()