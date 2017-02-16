import board
import ship

boardSize = 10
playerBoard = board.Board(boardSize)
computerBoard = board.Board(boardSize)
hitX = 1
hitY = 1
ship1 = ship.Ship(2, 3, 4, 'V')
ship2 = ship.Ship(5, 5, 3, 'H')


def start_game():
    print("Let's play Battleship!")


def print_game():
    print('-------------------')
    board.Board.print_board(computerBoard)
    print('===================')
    board.Board.print_board(playerBoard)
    print('-------------------')

# ------------------- MAIN -------------------

if __name__ == '__main__':
    start_game()
    print_game()
    playerBoard.place_ship(ship1)
    playerBoard.place_ship(ship2)
    print_game()
    print(playerBoard.attack_ship(3, 4))
    print(playerBoard.attack_ship(5, 6))
    print_game()