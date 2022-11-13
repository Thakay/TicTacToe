

#Data structure to store game states
gameBoard = {"top-L":"", "top":"", "top-R":"", 
            "mid-L":"", "mid":"", "mid-R":"", 
            "low-L":"", "low":"", "low-R":""}

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


    
