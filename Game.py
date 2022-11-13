

#Data structure to store game states
gameBoard = {"top-L":"X", "top":"X", "top-R":"X", 
            "mid-L":"", "mid":"O", "mid-R":"", 
            "low-L":"", "low":"", "low-R":"X"}

#Function to print the game board
def printBoard(board):
    print(board['top-L'].center(5) + '|'.ljust(3) + board['top'].center(1) + '|'.rjust(3) + board['top-R'].center(5))
    print('-----------------')
    print(board['mid-L'].center(5) + '|'.ljust(3) + board['mid'].center(1) + '|'.rjust(3) + board['mid-R'].center(5))
    print('-----------------')
    print(board['low-L'].center(5) + '|'.ljust(3) + board['low'].center(1) + '|'.rjust(3) + board['low-R'].center(5))

#printBoard(gameBoard)

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
print(logic(gameBoard))

    
