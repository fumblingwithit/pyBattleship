class Ship(object):
    """This class defines a ship"""

    def __init__(self, start_x, start_y, size, orientation):
        """The initializer for the class"""
        self.start_x = int(start_x)
        self.start_y = int(start_y)
        self.size = int(size)
        self.orientation = str(orientation)
        self.ship = []
        for ptr in range(0, self.size):
            self.ship.append(['S'])

    def show(self):
        """Shows the ship"""
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
            if self.orientation == 'H':
                x_coordinate = self.start_x
                for x_coordinate in range(self.start_x, self.start_x + self.size):
                    board.place_piece(x_coordinate, self.start_y)
            else:
                y_coordinate = self.start_y
                for y_coordinate in range(self.start_y, self.start_y + self.size):
                    board.place_piece(self.start_x, y_coordinate)

    def update(self, x_coordinate, y_coordinate, value):
        print('ship: ' + str(self.ship))
        print('X: ' + str(x_coordinate))
        print('Y: ' + str(y_coordinate))
        print('Orientation: ' + self.orientation)
        print('Length: ' + str(len(self.ship)))
        if self.orientation == 'H':
            if self.start_y == y_coordinate:
                self.ship.insert(x_coordinate, [value])
                temp_ship1 = self.ship[:x_coordinate].copy()
                temp_ship2 = self.ship[x_coordinate:].copy()
                #print('H T1 - 1')
                #print(temp_ship1)
                #print('H T2 - 1')
                #print(temp_ship2)
                temp_ship1.pop()
                temp_ship1.extend(temp_ship2)
                #print('H T1 - 2')
                #print(temp_ship1)
                #print('H T2 - 2')
                #print(temp_ship2)
                self.ship = temp_ship1.copy()
                print('H ship: ' + str(self.ship))
        else:
            if self.start_x == x_coordinate:
                self.ship.insert(y_coordinate, [value])
                temp_ship1 = self.ship[:y_coordinate].copy()
                temp_ship2 = self.ship[y_coordinate:].copy()
                print('V T1 - 1')
                print(temp_ship1)
                print('V T2 - 1')
                print(temp_ship2)
                temp_ship1.pop()
                temp_ship1.extend(temp_ship2)
                print('V T1 - 1')
                print(temp_ship1)
                print('V T2 - 1')
                print(temp_ship2)
                self.ship = temp_ship1.copy()
                print('V ship: ' + str(self.ship))
