"""This module contains my version of the game Battleship written in python3"""
__version__ = '0.1'
__author__ = 'Jon Brohauge'

import board
import ship

BOARDSIZE = 10
PLAYERBOARD = board.Board(BOARDSIZE)
COMPUTERBOARD = board.Board(BOARDSIZE)
HITX = 1
HITY = 1
SHIP1 = ship.Ship(2, 3, 4, 'V')
SHIP2 = ship.Ship(5, 5, 3, 'H')


def start_game():
    """Start the game"""
    print("Let's play Battleship!")
    PLAYERBOARD.place_ship(SHIP1)
    PLAYERBOARD.place_ship(SHIP2)


def print_game():
    """Print the game"""
    print('-------------------')
    board.Board.print_board(COMPUTERBOARD)
    print('===================')
    board.Board.print_board(PLAYERBOARD)
    print('-------------------')


# ------------------- MAIN -------------------

if __name__ == '__main__':
    start_game()
    print_game()
    print(PLAYERBOARD.attack_ship(3, 4))
    print(PLAYERBOARD.attack_ship(5, 6))
    print_game()
