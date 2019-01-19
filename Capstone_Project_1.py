
def display_board(board):
    print('Tic Tac Toe Board \n')
    print('_________')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('_________')

    
def usr_input():
    response='X'
    while (response=='X') or (response=='O'):
        player1_choice=input('What do u want to choose? X/O: ')
        if player1_choice=='X':
            player2_choice='O'
            print('Player1 will play with "X" and Player2 will play with "O"')
            return player1_choice,player2_choice
        elif player1_choice=='O':
            player2_choice='X'
            print('Player1 will play with "O" and Player2 will play with "X"')
            return player1_choice,player2_choice
        else:
            print('Invalid choice; Try Again')
            
def place_marker(board, marker, position):
    board[position] = marker   

def win_check(board,mark):
    #if board[1]==mark and board[2]==mark and board[3]==mark or board[4]==mark and board[5]==mark and board[6]==mark or board[7]==mark and board[8]==mark and board[9]==mark or board[1]==mark and board[4]==mark and board[7]==mark or board[2]==mark and board[5]==mark and board[8]==mark or board[3]==mark and board[6]==mark and board[9]==mark or board[1]==mark and board[5]==mark and board[9]==mark or board[3]==mark and board[5]==mark and board[7]==mark:
    if board[1]==board[2]==board[3]==mark or board[4]==board[5]==board[6]==mark or board[7]==board[8]==board[9]==mark or board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark or board[1]==board[5]==board[9]==mark or board[3]==board[5]==board[7]==mark:    
        return True
    else:
        return False
    
def space_check(board, position):    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    player=0
    pos=[1,2,3,4,5,6,7,8,9]
    while player not in pos or not space_check(board, player):
        player=input(f'Choice any position between 1 to 9: ')   
        player=int(player)
        pos.append(player)
            
    return player
       
    
def main_game():
     status=True
     while status:
        turn='Player1'
        theBoard = [' '] * 10
        player1_choice, player2_choice = usr_input()
    
        done=True
        while done:
            ready=input('Do u want to begin the game? y/n: ')
            if ready=='n':
                isExit=input('Do u want to quit? y/n: ')
                if isExit=='y':
                    print('Game End')
                    done=False
                    game_on=False
                    break
                elif isExit=='n':
                    continue
            else:
                print('Lets Begin')
                game_on = True
                break
        
        while game_on:
            if turn== 'Player1':
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_choice, position)
            
                if win_check(theBoard, player1_choice):
                    display_board(theBoard)
                    print('Congratulations! You have won the game!')
                    game_on = False
                    status = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('OOPPSS!!The game is a draw!')
                        status = False
                        break
                    else:
                        turn = 'Player2'
            else:
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_choice, position)

                if win_check(theBoard, player2_choice):
                    display_board(theBoard)
                    print('Player 2 has won!')
                    status = False
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        status = False
                        break
                    else:
                        turn = 'Player1'   
    
         
main_game()
