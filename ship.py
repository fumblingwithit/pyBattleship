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
                self.update(x_coordinate, y_coordinate, 'M')
                return 'Miss'
        else:
            return 'Dumb ASS! - you missed the board'

    def place(self, board):
        """Place a ship on the board"""
        if board.is_on_board(self.start_x, self.start_y):
            if self.orientation == 'V':
                x_coordinate = self.start_x
                for x_coordinate in range(self.start_x, self.start_x + self.size):
                    board.place_piece(x_coordinate, self.start_y)
            else:
                y_coordinate = self.start_y
                for y_coordinate in range(self.start_y, self.start_y + self.size):
                    board.place_piece(self.start_x, y_coordinate)

    def update(self, x_coordinate, y_coordinate, value):
        print('Ship: ' + str(self.ship))
        print('Orientation: ' + self.orientation)
        print('X: ' + str(x_coordinate))
        print('Y: ' + str(y_coordinate))
        print('Value: ' + value)

        if self.orientation == 'H':
            print('H - 1')
            print('Start_X: ' + str(self.start_x))
            print('Start_Y: ' + str(self.start_y))
            print('X: ' + str(x_coordinate))
            print('Y: ' + str(y_coordinate))
            if self.start_y == y_coordinate:
                self._place_mark(x_coordinate, value)
        else:
            if self.start_x == x_coordinate:
                print('V - 1')
                self._place_mark(y_coordinate, value)

    def _place_mark(self, index, value):
        print('---DEBUG MARK---')
        print('Ship: ' + str(self.ship))
        print('Orientation: ' + self.orientation)
        print('Index: ' + str(index))
        print('Value: ' + value)
        self.ship.insert(index, [value])
        temp_ship1 = self.ship[:index].copy()
        temp_ship2 = self.ship[index:].copy()
        temp_ship1.pop()
        temp_ship1.extend(temp_ship2)
        self.ship = temp_ship1.copy()
