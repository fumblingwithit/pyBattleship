class Board:
    def __init__(self, b):
        self.boardSize = b
        self.board = []

        for x in range(0, self.boardSize):
            self.board.append(["O"] * self.boardSize)

    def is_on_board(self, x, y):
        if (0 <= x < self.boardSize) and (0 <= y < self.boardSize):
            return True
        else:
            return False
