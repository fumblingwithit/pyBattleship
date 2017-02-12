#Stuff related to the game board itself goes here


class Board:
    boardSize = 0
    board = []

    def __init__(self, b):
        Board.boardSize = int(b)
        for x in range(0,self.boardSize):
            Board.board.append(["O"] * Board.boardSize)
