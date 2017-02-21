import board
import ship


BOARDSIZE = 10
PLAYERBOARD = board.Board(BOARDSIZE)
COMPUTERBOARD = board.Board(BOARDSIZE)
HITX = 1
HITY = 1
SHIP1 = ship.Ship("Motorlaunch", 2, 3, 3, 'V')
SHIP2 = ship.Ship("Carrier", 5, 5, 5, 'H')


def start_game():
    """Start the game"""
    print("Let's play Battleship!")


def print_game():
    """Print the game"""
    print('-------------------')
    board.Board.print(COMPUTERBOARD)
    print('===================')
    board.Board.print(PLAYERBOARD)
    print('-------------------')


# ------------------- MAIN -------------------

if __name__ == '__main__':
    start_game()
#    print_game()
    SHIP1.place(COMPUTERBOARD)
    SHIP2.place(PLAYERBOARD)

    print(SHIP1.attack(COMPUTERBOARD, 3, 4))
    print(SHIP2.attack(PLAYERBOARD, 6, 5))
    print_game()
    SHIP1.show()
    SHIP2.show()
    SHIP1.attack(COMPUTERBOARD, 2, 4)
    SHIP2.attack(PLAYERBOARD, 2, 4)
    print_game()
    SHIP1.show()
    SHIP2.show()
