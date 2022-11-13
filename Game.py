

#Data structure to store game states
gameBoard = {"top-L":"", "top":"", "top-R":"", 
            "mid-L":"", "mid":"", "mid-R":"", 
            "low-L":"", "low":"", "low-R":""}
moves = {"7":"top-L", "8":"top", "9": "top-R", 
        "4":"mid-L", "5":"mid", "6": "mid-R",
        "1":"low-L", "2":"low", "3": "low-R",}

#Function to print the game board
def printBoard(board):
    print(board['top-L'].center(5) + '|'.ljust(3) + board['top'].center(1) + '|'.rjust(3) + board['top-R'].center(5))
    print('-----------------')
    print(board['mid-L'].center(5) + '|'.ljust(3) + board['mid'].center(1) + '|'.rjust(3) + board['mid-R'].center(5))
    print('-----------------')
    print(board['low-L'].center(5) + '|'.ljust(3) + board['low'].center(1) + '|'.rjust(3) + board['low-R'].center(5))
    print('\n')



def logic(board: dict) -> str:

    if board.get('top-L') == board.get('top') == board.get('top-R'):
        return board.get('top')
    elif board.get('mid-L') == board.get('mid') == board.get('mid-R'):
        return board.get('mid')
    elif board.get('low-L') == board.get('low') == board.get('low-R'):
        return board.get('low')
    elif board.get('top-L') == board.get('mid-L') == board.get('low-L'):
        return board.get('top-L')
    elif board.get('top') == board.get('mid') == board.get('low'):
        return board.get('top')
    elif board.get('top-R') == board.get('mid-R') == board.get('low-R'):
        return board.get('top-R')
    elif board.get('top-L') == board.get('mid') == board.get('low-R'):
        return board.get('top-L')
    elif board.get('top-R') == board.get('mid') == board.get('low-L'):
        return board.get('top-R')
    else:
        return None

def move(board: dict, location: str, turn: str)->bool:
    if board.get(location) == "":
        board[location] = turn
        return True
    else:
        print("Invalid Move")
        return False

def play(board: dict,start: bool = 1):
    
    turn = start
    turns = ("X","O")
    print("Welcome to the TIC-TAC-TOE")
    print("Enter your move when your turn Numpad like:")
    print("7 8 9 ")
    print("4 5 6 ")
    print("1 2 3 ")
    print("Each number is mapped to the location on the board ex: 7 is top left", "\n")

    printBoard(board)
    for i in range(9):
        if turn:
            char = turns[0]
        else:
            char = turns[1]
        
        #Take Valid input
        while True:
            location = input(f"Its is {char}'s turn input your prefered location (1-9): ")
            user_i = moves.get(location)
            if user_i:
                move(board,user_i,char)
                break
            else:
                print("Invalid Move, Try Again!")

        printBoard(board)
        turn =  not turn
        res = logic(board)
        if res:
            print(f"{res} WON !!")
            break
        elif i == 8:
            print("Draw!")
    print("Game is over!")  


    
