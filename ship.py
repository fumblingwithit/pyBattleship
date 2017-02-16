class Ship:

    def __init__(self, startX, startY, size, orientation):
        self.startX = int(startX)
        self.startY = int(startY)
        self.size = int(size)
        self.orientation = str(orientation)
        self.ship = []
        for ptr in range(0, self.size):
          self.ship.append(['S'])

    def show_ship(self):
        for row in self.ship:
            print(" ".join(row))

