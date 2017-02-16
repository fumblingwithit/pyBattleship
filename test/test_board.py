import unittest
import board


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board_size = 10
        self.testBoard = board.Board(self.board_size)

    def test_create_board(self):
        self.assertEqual(self.board_size, self.testBoard.boardSize)

    def test_is_on_board(self):
        self.assertTrue(self.testBoard.is_on_board(2, 3))
        self.assertFalse(self.testBoard.is_on_board(99, 99))

    def test_is_piece_set(self):
        self.testBoard.place_piece(2, 3)
        self.assertTrue(self.testBoard.is_piece_set(2, 3))
        self.assertFalse(self.testBoard.is_piece_set(2, 2))
        self.assertFalse(self.testBoard.is_piece_set(3, 3))
        self.assertRaises(Exception, self.testBoard.place_piece, 2, 3)

if __name__ == '__main__':
    unittest.main()
