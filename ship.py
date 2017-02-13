class Ship:

    def __init__(self, sX, sY, s, o):
        self.startX = int(sX)
        self.startY = int(sY)
        self.size = int(s)
        self.orientation = str(o)
        self.ship = []
        for ptr in range(0, self.size):
          self.ship.append(["S"])

    def printShip(self):
        for row in self.ship:
            print(" ".join(row))

