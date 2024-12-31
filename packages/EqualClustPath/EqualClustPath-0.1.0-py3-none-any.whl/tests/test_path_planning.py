import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import numpy as np
from EqualClustPath.path_planning import nearest_neighbor_2opt, path_length

class TestPathPlanning(unittest.TestCase):
    def test_path_length(self):
        path = np.array([[0, 0], [1, 1], [2, 2], [0, 0]])
        length = path_length(path)
        self.assertAlmostEqual(length, 5.656854249492381, places=7)

    def test_nearest_neighbor_2opt(self):
        coords = np.array([[0, 0], [1, 1], [2, 2]])
        center_point = np.array([0, 0])
        path = nearest_neighbor_2opt(coords, center_point)
        self.assertEqual(len(path), 5)
        self.assertEqual(path[0].tolist(), center_point.tolist())
        self.assertEqual(path[-1].tolist(), center_point.tolist())

if __name__ == '__main__':
    unittest.main()
