import unittest

from iwpp.src.distance.distance_manhattan import ManhattanDistance


class TestManhattanDistance(unittest.TestCase):
    def test_manhattan_distance(self):
        manhattan = ManhattanDistance().calc_manhattan((0, 0), (0, 10))
        self.assertEqual(10, manhattan)


if __name__ == '__main__':
    unittest.main()
