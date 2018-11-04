import random, time

winner = None

def display_board(board):
    print('-------------')
    print(f'| {board[1]} | {board[2]} | {board[3]} |')
    print(f'| {board[4]} | {board[5]} | {board[6]} |')
    print(f'| {board[7]} | {board[8]} | {board[9]} |')
    print('-------------')
    
    
def game_start():
    
    player1 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input("Player ONE, please choose the symbol of your preference for the game: 'X' or 'O':  ").upper()
        
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return(player1, player2)

def choose_first():
    choice = random.choice([True, False])
    if choice:
        print('Player ONE, congrats! Random choise was on your side: you start the game.', end='\n\n')
    else:
        print('Player TWO, congrats! Random choise was on your side: you start the game.', end='\n\n')
    return choice

def make_turn(player):
    global board
    cellnumber = -10
    
    if board.count(' ') == 1:
        board[board.index(' ')] = player
        return
    while cellnumber not in range(1,10):
        try:
            while cellnumber not in range(1,10):
                cellnumber = int(input("Enter the number of the free cell you want to take in range 1-9: "))
            while board[cellnumber] != ' ':
                cellnumber = int(input("The cell is already taken, please enter the number of a free cell:  "))
        except:
            cellnumber = -10  # if some problems with input ---> put back the default value
            print("Please enter integer in range 1-9! Try again...")
        
    board[cellnumber] = player
    
    
    
def check_if_win(board, mark):
    wincomb = [mark,mark,mark]
    
    if board.count('X')<3 and board.count('O')<3:
        return False
    
    return ((board[1:4] == wincomb) or (board[4:7] == wincomb) or (board[7:10] == wincomb) or # horisontals
    (board[1:9:3] == wincomb) or (board[2:10:3] == wincomb) or (board[3:10:3] == wincomb) or # verticals
    (board[1:10:4] == wincomb) or (board[3:9:2] == wincomb)) # diagonals
    
    
    
#### MAIN PART (LOGIC OF THE GAME HERE):

while( winner == None):
    board_instruction = ['*', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    players = game_start()

    print()
    print('Here is the way our game field looks like: to each cell corresponds a certain number:',end = '\n\n')
    display_board(board_instruction)

    print("Determining which player starts...", end='\n\n')
    time.sleep(1)

    turn = choose_first()


    while winner == None:
    
        if(turn):
            print('Player ONE: ', end='')
            make_turn(players[0])
            turn = False
            print('\n'*100)
            display_board(board)
            if check_if_win(board, players[0]):
                print('Player ONE: Congratulations, you are the winner!')
                break
                local_winner = 'Player ONE'
        
        
        else:
            print('Player TWO:')
            make_turn(players[1])
            turn = True
            print('\n'*100)
            display_board(board)
            if check_if_win(board, players[1]):
                print('Player TWO: Congratulations, you are the winner!')
                break
                local_winner = 'Player TWO'
        if ' ' not in board:
            print('It is a draw. Nobody won. Both of you are loosers. Haha')
            break
    
    time.sleep(2)
    print()
    if input("Do you want to repeat the game?: 'y'= yes 'n' = no:  ") == 'n':
        #winner = local_winner
        break
