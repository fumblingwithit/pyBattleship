import unittest
import ship


class ShipTest(unittest.TestCase):

    def setUp(self):
        self.start_x = 1
        self.start_y = 1
        self.size = 3
        self.orientation = 'H'
        self.testShip = ship.Ship(self.start_x, self.start_y, self.size, self.orientation)

    def test_create_ship(self):
        self.assertEqual(self.start_x, self.testShip.startX)
        self.assertEqual(self.start_x, self.testShip.startX)
        self.assertEqual(self.start_y, self.testShip.startY)
        self.assertEqual(self.size, self.testShip.size)
        self.assertEqual(self.orientation, self.testShip.orientation)

    def test_show_ship(self):
        self.assertTrue(True,'Not implemented yet')

if __name__ == '__main__':
    unittest.main()
