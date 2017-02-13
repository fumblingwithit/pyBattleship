import board
import ship

demoBoardSize = 5
demoBoard = board.Board(demoBoardSize)
hitX = 1
hitY = 1
ship1 = ship.Ship(0, 0, 3, 'V')


def start_game():
    print("Let's play Battleship!")
   # self.print_board(board)


class Battleship:

    def is_ship_hit(ship, targetX, targetY):
        if (targetX < ship.startX or targetX > (ship.startX + ship.size)) or (
                targetY < ship.startY or targetY > (ship.startY + ship.size)):
            return False
        else:
            print('startX: %s startY: %s' % (ship.startX, ship.startY))
            print('endX: %s endY: %s' % (ship.startX + ship.size, ship.startY + ship.size))
            print('targetX: %s targetY: %s' % (targetX, targetY))
            return True

    def print_board(board):
        for row in board:
            print(" ".join(row))

# ------------------- MAIN -------------------

print("Let's play Battleship!")
