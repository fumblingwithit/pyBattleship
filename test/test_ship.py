import unittest
import ship


class ShipTest(unittest.TestCase):

    def test_create_ship(self):
        start_x = 1
        start_y = 1
        size = 3
        orientation = "horizontal"
        test_ship = ship.Ship(start_x, start_y, size, orientation)
        self.assertEqual(start_x, test_ship.startX)
        self.assertEqual(start_x, test_ship.startX)
        self.assertEqual(start_y, test_ship.startY)
        self.assertEqual(size, test_ship.size)
        self.assertEqual(orientation, test_ship.orientation)

if __name__ == '__main__':
    unittest.main()
