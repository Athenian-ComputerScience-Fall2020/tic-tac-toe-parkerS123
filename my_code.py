# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.

tictactoe = {'TL': '', 'TM': '', 'TR': '', 'ML': '', 'MM': '', 'MR': '', 'BL': '', 'BM': '', 'BR': '',}

def tictactoe_function(tictactoe): 
    print(" | | ")
    print("-+-+-")
    print(" | | ")
    print("-+-+-")
    print(" | | ")
    user_move = input("make a move but entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")

    while True:
        if user_move == 'TL' or user_move == 'TM' or user_move == 'TR' or user_move == 'ML' or user_move == 'MM' or user_move == 'MR' or user_move == 'BL' or user_move == 'BM' or user_move == 'BR': 
            tictactoe[user_move] = 'x' 
            break
        else: 
            print("Please enter a valid move next time...")
            user_move = input("make a move but entering TL, TM, TR, ML, MM, MR, BL, BM, BR: ")



tictactoe_function(tictactoe)