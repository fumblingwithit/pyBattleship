import unittest
import ship
import board


class ShipTest(unittest.TestCase):
    def setUp(self):
        self.start_x = 1
        self.start_y = 1
        self.size = 3
        self.orientation = 'H'
        self.testShip1 = ship.Ship('testShip1', self.start_x, self.start_y, self.size, self.orientation)
        self.testShip2 = ship.Ship('testShip2', self.start_x+1, self.start_y+1, self.size, 'V')
        self.testBoard = board.Board(10)
        self.testShip1.place(self.testBoard)
        self.testShip2.place(self.testBoard)

    def test_create_ship(self):
        self.assertEqual(self.start_x, self.testShip1.start_x)
        self.assertEqual(self.start_y, self.testShip1.start_y)
        self.assertEqual(self.size, self.testShip1.size)
        self.assertEqual(self.orientation, self.testShip1.orientation)

    def test_is_ship_hit(self):
        self.assertEqual(self.testShip1.attack(self.testBoard, 1, 1), 'Hit')
        self.assertEqual(self.testShip1.attack(self.testBoard, 3, 3), 'Miss')
        self.assertEqual(self.testShip2.attack(self.testBoard, 2, 2), 'Hit')
        self.assertEqual(self.testShip2.attack(self.testBoard, 2, 5), 'Miss')


if __name__ == '__main__':
    unittest.main()
