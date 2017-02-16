class Board:
    def __init__(self, b):
        self.boardSize = b
        self.board = []

        for x in range(0, self.boardSize):
            value = str(x)
            self.board.append(['O'] * self.boardSize)
#            self.board.append([value] * self.boardSize)

    def is_on_board(self, x, y):
        if (0 <= x < self.boardSize) and (0 <= y < self.boardSize):
            return True
        else:
            return False

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def place_ship(self, ship):
        if self.is_on_board(ship.startX, ship.startY):
            if ship.orientation == "V":
                x = ship.startX
                for x in range(ship.startX, ship.startX+ship.size):
                    self.place_piece(x, ship.startY)
            else:
                y = ship.startY
                for y in range(ship.startY, ship.startY + ship.size):
                    self.place_piece(ship.startX, y)

        return True

    def place_piece(self, x, y):
        try:
            if not self.is_on_board(x, y):
                raise Exception('not_on_board')
            if self.is_piece_set(x, y):
                raise Exception('piece_is_set')
            self.board[x].insert(y, 'S')
            temp_board1 = self.board[x][:y].copy()
            temp_board2 = self.board[x][y:].copy()
            temp_board1.pop()
            temp_board1.extend(temp_board2)
            self.board[x] = temp_board1
        except ValueError as err:
            print(err.args)

    def is_piece_set(self, x, y):
        if self.is_on_board(x, y):
            if str(self.board[x][y-1]) == "S":
                return True
            else:
                return False