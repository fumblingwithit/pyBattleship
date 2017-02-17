class Board(object):
    """This class defines the board"""

    def __init__(self, board_size):
        """The initializer for the class"""
        self.board_size = board_size
        self.board = []

        for index in range(0, self.board_size):
            value = str(index)
            self.board.append(['O'] * self.board_size)

    def is_on_board(self, x_coordinate, y_coordinate):
        """Is the piece on the board"""
        return bool((0 <= x_coordinate < self.board_size) and (0 <= y_coordinate < self.board_size))

    def print_board(self):
        """Print the board"""
        for row in self.board:
            print(" ".join(row))

    def place_ship(self, ship):
        """Place a ship on the board"""
        if self.is_on_board(ship.start_x, ship.start_y):
            if ship.orientation == 'V':
                x_coordinate = ship.start_x
                for x_coordinate in range(ship.start_x, ship.start_x + ship.size):
                    self._place_piece(x_coordinate, ship.start_y)
            else:
                y_coordinate = ship.start_y
                for y_coordinate in range(ship.start_y, ship.start_y + ship.size):
                    self._place_piece(ship.start_x, y_coordinate)

    def update_piece(self, x_coordinate, y_coordinate, value):
        """Update the placement of the ship on the board"""
        self.board[x_coordinate].insert(y_coordinate, value)
        temp_board1 = self.board[x_coordinate][:y_coordinate].copy()
        temp_board2 = self.board[x_coordinate][y_coordinate:].copy()
        temp_board1.pop()
        temp_board1.extend(temp_board2)
        self.board[x_coordinate] = temp_board1

    def _place_piece(self, x_coordinate, y_coordinate):
        """Place a piece of the ship on the board"""
        try:
            if not self.is_on_board(x_coordinate, y_coordinate):
                raise Exception('not_on_board')
            if self.is_piece_set(x_coordinate, y_coordinate):
                raise Exception('piece_is_set')
            self.update_piece(x_coordinate, y_coordinate, 'S')
        except ValueError as err:
            print(err.args)

    def is_piece_set(self, x_coordinate, y_coordinate):
        """Check to see if a piece is set """
        if self.is_on_board(x_coordinate, y_coordinate):
            return bool(str(self.board[x_coordinate][y_coordinate - 1]) != 'O')

    def attack_ship(self, x_coordinate, y_coordinate):
        """Place a hit"""
        if self.is_on_board(x_coordinate, y_coordinate):
            if self.is_piece_set(x_coordinate, y_coordinate):
                self.update_piece(x_coordinate, y_coordinate, 'X')
                return 'Hit'
            else:
                return 'Miss'
