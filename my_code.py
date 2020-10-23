# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# Megan
# A note on style: Dictionaries can be defined before or after functions.

tictactoe = {'TL': '', 'TM': '', 'TR': '', 'ML': '', 'MM': '', 'MR': '', 'BL': '', 'BM': '', 'BR': '',}
ok_moves = ['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR']

def tictactoe_function(tictactoe): 
    print(tictactoe['TL'] + " |" + tictactoe['TM'] + " | " + tictactoe["TR"])
    print("-+-+-")
    print(tictactoe['ML'] + " |" + tictactoe['MM'] + " | " + tictactoe["MR"])
    print("-+-+-")
    print(tictactoe['BL'] + " |" + tictactoe['BM'] + " | " + tictactoe["BR"])
tictactoe_function(tictactoe) 

def three_in_a_row(tictactoe):
    if {'TL': 'x', 'TM': 'x', 'TR': 'x'}: 
        return True
    if {'TL': 'o', 'TM': 'o', 'TR': 'o'}:
        return True
    if {'ML': 'x', 'MM': 'x', 'MR': 'x'}:
        return True
    if {'ML': 'o', 'MM': 'o', 'MR': 'o'}:
        return True
    if {'BL': 'x', 'BM': 'x', 'BR': 'x'}:
        return True
    if {'BL': 'o', 'BM': 'o', 'BR': 'o'}:
        return True
    # continue with verticle and diagonal, then return false
    

#three_in_a_row = '1'

while three_in_a_row == False: 
    print("X's goes first!")   
    x_move = input("X's make a move but entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")
    o_move = 'nothing'

    while True:
        if x_move in ok_moves:
            ok_moves.remove(x_move)
            tictactoe[x_move] = 'x' 
            break
        else: 
            print("Please enter a valid move next time...")
            x_move = input("make a move but entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")

        o_move = input("O's make a move but entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")

    while True:
        if o_move in ok_moves:
            ok_moves.remove(o_move)
            tictactoe[o_move] = 'o' 
            break
        else: 
            print("Please enter a valid move next time...")
            o_move = input("make a move but entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")



print(tictactoe)
tictactoe_function(tictactoe)