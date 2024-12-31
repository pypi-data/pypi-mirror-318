import numpy as np
from sklearn.cluster import KMeans

def generate_data(n_samples, x_range, y_range):
    """
    生成模拟数据
    :param n_samples: 生成的样本数量
    :param x_range: x坐标的范围（最小值，最大值）
    :param y_range: y坐标的范围（最小值，最大值）
    :return: x 和 y 坐标
    """
    x = np.random.uniform(x_range[0], x_range[1], n_samples)
    y = np.random.uniform(y_range[0], y_range[1], n_samples)
    return x, y

def balanced_kmeans(data, num_clusters, tolerance=2, max_iterations=100):
    """
    执行均衡 K-means 聚类
    :param data: 输入数据点
    :param num_clusters: 聚类数量
    :param tolerance: 容差范围
    :param max_iterations: 最大迭代次数
    :return: 聚类结果
    """
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++')
    kmeans.fit(data)
    centroids = kmeans.cluster_centers_

    clusters = initial_assignment(data, centroids, num_clusters)
    labels = np.full(len(data), -1, dtype=int)
    for i, indices in clusters.items():
        for idx in indices:
            labels[idx] = i

    # 处理未分配的数据点
    unassigned = set(range(len(data))) - set(idx for indices in clusters.values() for idx in indices)
    for idx in unassigned:
        closest_centroid = np.argmin([np.linalg.norm(data[idx] - centroid) for centroid in centroids])
        clusters[closest_centroid].append(idx)
        labels[idx] = closest_centroid

    return clusters, kmeans, labels

def initial_assignment(data, centroids, num_clusters):
    """
    初步分配数据点
    :param data: 输入数据点
    :param centroids: 初始质心
    :param num_clusters: 聚类数量
    :return: 初步分配的簇
    """
    n = len(data)
    base_size = n // num_clusters  # 每个簇的基础数据量
    extra_count = n % num_clusters  # 需要多分配一个数据点的簇数量
    clusters = {i: [] for i in range(num_clusters)}
    distances = np.array([[np.linalg.norm(x - centroids[j]) for j in range(num_clusters)] for x in data])

    assigned = set()
    for i in range(num_clusters):
        sorted_indices = np.argsort(distances[:, i])
        count = base_size + (1 if i < extra_count else 0)  # 多分配一个数据点的簇
        for idx in sorted_indices:
            if len(clusters[i]) < count and idx not in assigned:
                clusters[i].append(idx)
                assigned.add(idx)

    return clusters

def cluster_data(x, y, num_clusters):
    """
    对数据进行聚类
    :param x: x坐标
    :param y: y坐标
    :param num_clusters: 聚类数量
    :return: 坐标点、聚类标签、聚类中心
    """
    coords = np.column_stack((x, y))
    clusters, kmeans, labels = balanced_kmeans(coords, num_clusters, tolerance=2)
    return coords, labels, kmeans.cluster_centers_
