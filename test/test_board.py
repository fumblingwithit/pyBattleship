# Unit tests of the board goes here
import unittest
import board


class BoardTest(unittest.TestCase):

    def test_board(self):
        boardSize = 10
        board.Board(boardSize)
        self.assertEqual(boardSize, board.Board.boardSize)

if __name__ == '__main__':
    unittest.main()
