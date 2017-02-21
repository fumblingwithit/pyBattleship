class Board(object):
    """This class defines the board"""

    def __init__(self, board_size):
        """The initializer for the class"""
        self.board_size = board_size
        self.board = []

        for index in range(0, self.board_size):
            self.board.append(['O'] * self.board_size)

    def is_on_board(self, x_coordinate, y_coordinate):
        """Is the piece on the board"""
        return bool((0 <= x_coordinate < self.board_size) and (0 <= y_coordinate < self.board_size))

    def print(self):
        """Print the board"""
        for row in self.board:
            print(" ".join(row))

    def update_piece(self, x_coordinate, y_coordinate, value):
        """Update the placement of the ship on the board"""
        self.board[y_coordinate][x_coordinate] = value

    def place_piece(self, x_coordinate, y_coordinate):
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
            return bool(str(self.board[y_coordinate][x_coordinate]) != 'O')
