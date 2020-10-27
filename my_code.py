# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# Megan
# A note on style: Dictionaries can be defined before or after functions.

tictactoe = {'TL': '', 'TM': '', 'TR': '', 'ML': '', 'MM': '', 'MR': '', 'BL': '', 'BM': '', 'BR': '',} #my dictionary of moves
ok_moves = ['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR'] #moves the user is allowed to make

print("This is a tictactoe game! Someone will be x's and someone will be o's.")
print("X's goes first!") 

def tictactoe_function(tictactoe): #function that creates the board
    print(tictactoe['TL'] + " |" + tictactoe['TM'] + " | " + tictactoe["TR"])
    print("-+-+-")
    print(tictactoe['ML'] + " |" + tictactoe['MM'] + " | " + tictactoe["MR"])
    print("-+-+-")
    print(tictactoe['BL'] + " |" + tictactoe['BM'] + " | " + tictactoe["BR"])
tictactoe_function(tictactoe) 

def three_in_a_row(tictactoe): #function that checks if a player won by looking for all possible ways to win
    if tictactoe['TL'] == 'x' and tictactoe['TM'] == 'x' and tictactoe['TR'] == 'x': 
        return True
    elif tictactoe['TL'] == 'o' and tictactoe['TM'] == 'o' and tictactoe['TR'] == 'o':
        return True
    elif tictactoe['ML'] == 'x' and tictactoe['MM'] == 'x' and tictactoe['MR'] == 'x': 
        return True
    elif tictactoe['ML'] == 'o' and tictactoe['MM'] == 'o' and tictactoe['MR'] == 'o':
        return True
    elif tictactoe['BL'] == 'x' and tictactoe['BM'] == 'x' and tictactoe['BR'] == 'x':
        return True
    elif tictactoe['BL'] == 'o' and tictactoe['BM'] == 'o' and tictactoe['BR'] == 'o':
        return True
    elif tictactoe['TL'] == 'x' and tictactoe['ML'] == 'x' and tictactoe['BL'] == 'x':
        return True
    elif tictactoe['TL'] == 'o' and tictactoe['ML'] == 'o' and tictactoe['BL'] == 'o':
        return True
    elif tictactoe['TM'] == 'x' and tictactoe['MM'] == 'x' and tictactoe['BM'] == 'x':
        return True
    elif tictactoe['TM'] == 'o' and tictactoe['MM'] == 'o' and tictactoe['BM'] == 'o':
        return True
    elif tictactoe['TR'] == 'x' and tictactoe['MR'] == 'x' and tictactoe['BR'] == 'x':
        return True
    elif tictactoe['TR'] == 'o' and tictactoe['MR'] == 'o' and tictactoe['BR'] == 'o':
        return True
    elif tictactoe['TL'] == 'x' and tictactoe['MM'] == 'x' and tictactoe['BR'] == 'x':
        return True
    elif tictactoe['TL'] == 'o' and tictactoe['MM'] == 'o' and tictactoe['BR'] == 'o':
        return True
    elif tictactoe['TR'] == 'x' and tictactoe['MM'] == 'x' and tictactoe['BL'] == 'x':
        return True
    elif tictactoe['TR'] == 'o' and tictactoe['MM'] == 'o' and tictactoe['BL'] == 'o':
        return True
    else:
        return False
outcome = three_in_a_row(tictactoe) #assigns function above to a variable
moves = 0 #keeps track of number of moves by both users

while outcome == False: 
    x_move = input("X's make a move by entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")

    while True:
        if x_move in ok_moves:
            ok_moves.remove(x_move) #removes the move they just made from ok moves so that place can't be plsyed again
            tictactoe[x_move] = 'x' 
            break
        else: 
            print("Please enter a valid move next time...")
            x_move = input("make a move by entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")
    tictactoe_function(tictactoe) #prints the board
    outcome = three_in_a_row(tictactoe) #reassigns outcome to check if outcome is now true
    moves = moves + 1 #adds a move
    if moves == 9 and outcome == False: #if there are 9 moves and nobody has won then it is a tie
        print("It's a tie!")
        tictactoe_function(tictactoe)
        break

    if outcome == True: #if outcome is now true that means somebody won
        print("Game Over!")
        tictactoe_function(tictactoe)
        break

    o_move = input("O's make a move by entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")

    while True:
        if o_move in ok_moves:
            ok_moves.remove(o_move)
            tictactoe[o_move] = 'o' 
            break
        else: 
            print("Please enter a valid move next time...")
            o_move = input("make a move by entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")
    tictactoe_function(tictactoe)
    outcome = three_in_a_row(tictactoe)
    moves = moves + 1
    
    if outcome == True:
        print("Game Over!")
        tictactoe_function(tictactoe)
        break
    
    if moves == 9 and outcome == False:
        print("It's a tie!")
        tictactoe_function(tictactoe)
        break
