import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import numpy as np
from EqualClustPath.clustering import generate_data, balanced_kmeans, initial_assignment


class TestClustering(unittest.TestCase):
    def test_generate_data(self):
        x, y = generate_data(150, [0, 10], [0, 10])
        self.assertEqual(len(x), 150)
        self.assertEqual(len(y), 150)
        self.assertTrue(np.all(x >= 0) and np.all(x <= 10))
        self.assertTrue(np.all(y >= 0) and np.all(y <= 10))

    def test_balanced_kmeans(self):
        test_cases = [
            (150, 3),  # 150 数据点，分 3 簇
            (152, 3),  # 152 数据点，分 3 簇，不可整除
            (200, 4),  # 200 数据点，分 4 簇
            (308, 6),  # 205 数据点，分 5 簇，不可整除
            (500, 7)  # 300 数据点，分 7 簇，不可整除
        ]

        for n_samples, num_clusters in test_cases:
            with self.subTest(n_samples=n_samples, num_clusters=num_clusters):
                x, y = generate_data(n_samples, [0, 10], [0, 10])
                coords = np.column_stack((x, y))
                clusters, kmeans, labels = balanced_kmeans(coords, num_clusters)
                total_points = sum([len(indices) for indices in clusters.values()])
                self.assertEqual(total_points, n_samples)
                self.assertEqual(len(clusters), num_clusters)

                # 检查每个簇的数据点数量
                base_size = n_samples // num_clusters
                extra_count = n_samples % num_clusters
                for i, indices in clusters.items():
                    if i < extra_count:
                        self.assertEqual(len(indices), base_size + 1)
                    else:
                        self.assertEqual(len(indices), base_size)


if __name__ == '__main__':
    unittest.main()
