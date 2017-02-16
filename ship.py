class Ship:

    def __init__(self, startX, startY, s, o):
        self.startX = int(startX)
        self.startY = int(startY)
        self.size = int(s)
        self.orientation = str(o)
        self.ship = []
        for ptr in range(0, self.size):
          self.ship.append(['S'])

    def printShip(self):
        for row in self.ship:
            print(" ".join(row))

