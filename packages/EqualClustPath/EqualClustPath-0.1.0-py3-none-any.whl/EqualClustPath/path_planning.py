import numpy as np


def path_length(path):
    """
    计算路径长度
    :param path: 路径点坐标
    :return: 路径总长度
    """
    total_length = 0
    for i in range(len(path) - 1):
        total_length += np.linalg.norm(path[i] - path[i + 1])
    return total_length


def nearest_neighbor_2opt(coords, center_point):
    """
    最近邻-2opt算法进行路径规划
    :param coords: 坐标点
    :param center_point: 中心点坐标
    :return: 优化后的路径
    """
    num_points = len(coords)
    path = np.zeros((num_points + 2, 2))
    current_pos = center_point
    visited = np.zeros(num_points, dtype=bool)

    path[0] = center_point
    for i in range(num_points):
        distances = np.linalg.norm(coords - current_pos, axis=1)
        distances[visited] = np.inf
        idx = np.argmin(distances)
        current_pos = coords[idx]
        path[i + 1] = current_pos
        visited[idx] = True

    path[-1] = center_point

    # 2-opt算法优化路径
    improved = True
    while improved:
        improved = False
        for i in range(1, num_points):
            for j in range(i + 1, num_points + 1):
                new_length = path_length(np.concatenate((path[:i], path[i:j + 1][::-1], path[j + 1:])))
                if new_length < path_length(path):
                    path = np.concatenate((path[:i], path[i:j + 1][::-1], path[j + 1:]))
                    improved = True
    return path
