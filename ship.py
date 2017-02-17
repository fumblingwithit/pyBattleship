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

    def show_ship(self):
        """Shows the ship"""
        for row in self.ship:
            print(" ".join(row))
