class Ship(object):
    """This class defines a ship"""

    def __init__(self, name, start_x, start_y, size, orientation):
        """The initializer for the class"""
        self.name = name
        self.start_x = int(start_x)
        self.start_y = int(start_y)
        self.size = int(size)
        self.orientation = str(orientation)
        self.ship = []
        for ptr in range(0, self.size):
            self.ship.append(['S'])

    def debug(self, x_coordinate, y_coordinate, value):
        print('===DEBUG===')
        self.show()
        print('X: ' + str(x_coordinate) + '(' + str(self.start_x) + ')')
        print('Y: ' + str(y_coordinate) + '(' + str(self.start_y) + ')')
        print('Value: ' + value)

    def show(self):
        """Shows the ship"""
        print('Name: ' + self.name)
        print('Orientation: ' + str(self.orientation))
        print('Length: ' + str(self.size))
        print(self.ship)

    def attack(self, board, x_coordinate, y_coordinate):
        """Place a hit"""
        if board.is_on_board(x_coordinate, y_coordinate):
            if board.is_piece_set(x_coordinate, y_coordinate):
                board.update_piece(x_coordinate, y_coordinate, 'X')
                self.update(x_coordinate, y_coordinate, 'X')
                return 'Hit'
            else:
                board.update_piece(x_coordinate, y_coordinate, 'M')
                return 'Miss'
        else:
            return 'Dumb ASS! - you missed the board'

    def place(self, board):
        """Place a ship on the board"""
        if board.is_on_board(self.start_x, self.start_y):
            if self.orientation == 'H':
                x_coordinate = self.start_x
                for x_coordinate in range(self.start_x, self.start_x + self.size):
                    board.place_piece(x_coordinate, self.start_y)
            else:
                y_coordinate = self.start_y
                for y_coordinate in range(self.start_y, self.start_y + self.size):
                    board.place_piece(self.start_x, y_coordinate)

    def update(self, x_coordinate, y_coordinate, value):
        #self.debug(x_coordinate, y_coordinate, value)
        if self.orientation == 'H':
            if self.start_y == y_coordinate:
                self.ship[x_coordinate-self.start_x] = [value]
        else:
            if self.start_x == x_coordinate:
                self.ship[y_coordinate-self.start_y] = [value]
