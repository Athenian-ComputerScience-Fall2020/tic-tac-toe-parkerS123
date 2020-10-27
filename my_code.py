# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# Megan
# A note on style: Dictionaries can be defined before or after functions.

tictactoe = {'TL': '', 'TM': '', 'TR': '', 'ML': '', 'MM': '', 'MR': '', 'BL': '', 'BM': '', 'BR': '',}
ok_moves = ['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR']

print("This is a tictactoe game! Someone will be x's and someone will be o's.")

def tictactoe_function(tictactoe): 
    print(tictactoe['TL'] + " |" + tictactoe['TM'] + " | " + tictactoe["TR"])
    print("-+-+-")
    print(tictactoe['ML'] + " |" + tictactoe['MM'] + " | " + tictactoe["MR"])
    print("-+-+-")
    print(tictactoe['BL'] + " |" + tictactoe['BM'] + " | " + tictactoe["BR"])
tictactoe_function(tictactoe) 

def three_in_a_row(tictactoe):
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
outcome = three_in_a_row(tictactoe)
print(outcome)
moves = 0

while outcome == False: 
    print("X's goes first!")   
    x_move = input("X's make a move by entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")
    o_move = 'nothing'

    while True:
        if x_move in ok_moves:
            ok_moves.remove(x_move)
            tictactoe[x_move] = 'x' 
            break
        else: 
            print("Please enter a valid move next time...")
            x_move = input("make a move by entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")
    tictactoe_function(tictactoe)

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

    if outcome == True:
        print("Game Over!")
        tictactoe_function(tictactoe)
        break

    moves = moves + 1
    if moves == 9 and outcome == False:
        print("It's a tie!")
        tictactoe_function(tictactoe)


# print(tictactoe)
tictactoe_function(tictactoe)