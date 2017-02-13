import unittest
import board


class BoardTest(unittest.TestCase):
    board_size = 10
    board.Board(board_size)

    def test_create_board(self):
        self.assertEqual(BoardTest.board_size, board.Board(self.board_size).boardSize)

    def test_is_on_board(self):
        self.assertTrue(board.Board(self.board_size).is_on_board(2, 3))
        self.assertFalse(board.Board(self.board_size).is_on_board(99, 99))

if __name__ == '__main__':
    unittest.main()
