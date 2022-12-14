from re import X
from array import *

def game():
    while True:
        # 2D arrary to represent tictactoe game board
        ttt_board = [
                     ['a', 'b', 'c'],
                     ['d', 'e', 'f'],
                     ['g', 'h', 'i']
                    ]
        # Find dimension/size of board (traditionally 3x3 but added to accommodate other sizes)
        board_size = len(ttt_board[0])
       
        # Game intro & starting board presentation
        print("\n\nLet's play tic tac toe! Each position on the board is represented by a letter.")
        print("Please review the game board below & choose your position accordingly. Player X is first!\n")
        
        for row in ttt_board:
            for val in row:
                print(val, end=" ")
            print()

        # default starting player is X
        player = 'X'
        
        # while no winning combos are present & there are open positions, continue game
        full_game_board = False
        no_winning_combo = True
        game_turns = 0

        while full_game_board == False and no_winning_combo == True:

            # player picks the letter associated with the spot they'd like to choose
            position = input(f"\nPlayer {player}, choose your position: ")
            print("")
            
            # check if chosen position is valid & available
            if position == 'O' or position == 'X' or position == None or position == '':
                print('Invalid option inputted. Try again.')
                continue
            
            valid = False
            for row in ttt_board:
                for val in row:
                    if position == val:
                        valid = True

            if not valid:
                print('Invalid option inputted. Try again.')
                continue

        # index/coordinates of the chosen letter are found
        # else:
            for i, j in enumerate(ttt_board):
                if position in j:
                    index = (i,j.index(position))
                    break
            
        # update board accordingly using the coordinates of the letter found above
            ttt_board[index[0]][index[1]] = player

        # view updated game board
            for row in ttt_board:
                for val in row:
                    print(val, end = " ")
                print()

        # check game status
            # check for 3 in a row aka winning combo
            
            # horizontally
            x = 0
            y = 0
            last_val = ''
            
            while x < board_size:
                match_count = 0
                last_val = ''

                while y < board_size :

                    if ttt_board[x][y] == last_val:
                        match_count += 1

                    if match_count == 2:
                        no_winning_combo = False
                        print(f"\nPlayer {player} wins horizontally!")

                    last_val = ttt_board[x][y]
                    y+=1

                y = 0
                x+= 1
            
            # vertically
            x = 0
            y = 0
            last_val = ''

            while y < board_size:
                match_count = 0
                last_val = ''

                while x < board_size:

                    if ttt_board[x][y] == 'O' or ttt_board[x][y] == 'X':
                        if ttt_board[x][y] == last_val:
                            match_count += 1
                        
                    if match_count == 2:
                        no_winning_combo = False
                        print(f"\nPlayer {player} wins vertically!")

                    last_val = ttt_board[x][y]
                    x+=1

                x = 0
                y+= 1

            # diagonally L to R
            x = 0
            y = 0
            last_val = ''

            while x < board_size:
                match_count = 0
                last_val = ''

                while y < board_size:
                    
                    if ttt_board[x][y] == 'O' or ttt_board[x][y] == 'X':
                        if ttt_board[x][y] == last_val:
                            match_count += 1

                    if match_count == 2:
                        no_winning_combo = False
                        print(f"\nPlayer {player} wins diagonally (L to R)!")

                    last_val = ttt_board[x][y]
                    x+= 1
                    y+= 1
            
            # diagonally R to L
            x = 0
            y = board_size - 1      # =2
            last_val = ''

            while x < board_size:
                match_count = 0
                last_val = ''

                while y >= 0:

                    if ttt_board[x][y] == 'O' or ttt_board[x][y] == 'X':
                        if ttt_board[x][y] == last_val:
                            match_count += 1

                    if match_count == 2:
                        no_winning_combo = False
                        print(f"\nPlayer {player} wins diagonally (R to L)!")

                    last_val = ttt_board[x][y]
                    x+= 1
                    y-= 1
                    
            # check for full game board
            game_turns += 1

            if no_winning_combo == True:
                if game_turns == 9:
                   full_game_board = True
                   print("\nTie game! Play again.")

        # switching players
            if player == "X":
                player = "O"
            else:
                player = "X"
 
game()
