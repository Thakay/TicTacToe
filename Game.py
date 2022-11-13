

gameBoard = {"top-L":"", "top":"", "top-R":"", 
            "mid-L":"", "mid":"", "mid-R":"", 
            "low-L":"", "low":"", "low-R":""}

def printBoard(board):
    print(board['top-L'].center(5) + '|'.ljust(3) + board['top'].center(1) + '|'.rjust(3) + board['top-R'].center(5))
    print('-----------------')
    print(board['mid-L'].center(5) + '|'.ljust(3) + board['mid'].center(1) + '|'.rjust(3) + board['mid-R'].center(5))
    print('-----------------')
    print(board['low-L'].center(5) + '|'.ljust(3) + board['low'].center(1) + '|'.rjust(3) + board['low-R'].center(5))

printBoard(gameBoard)

