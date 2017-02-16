import unittest
import board


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board_size = 10
        self.testBoard = board.Board(self.board_size)
        self.testBoard.place_piece(2, 3)

    def test_create_board(self):
        self.assertEqual(self.board_size, self.testBoard.boardSize)

    def test_is_on_board(self):
        self.assertTrue(self.testBoard.is_on_board(2, 3))
        self.assertFalse(self.testBoard.is_on_board(99, 99))

    def test_is_piece_set(self):
        self.assertTrue(self.testBoard.is_piece_set(2, 3))
        self.assertFalse(self.testBoard.is_piece_set(2, 2))
        self.assertFalse(self.testBoard.is_piece_set(3, 3))
        self.assertRaises(Exception, self.testBoard.place_piece, 2, 3)

    def test_is_ship_hit(self):
        self.assertEqual(self.testBoard.attack_ship(2, 3), 'Hit')
        self.assertEqual(self.testBoard.attack_ship(3, 3), 'Miss')

if __name__ == '__main__':
    unittest.main()
