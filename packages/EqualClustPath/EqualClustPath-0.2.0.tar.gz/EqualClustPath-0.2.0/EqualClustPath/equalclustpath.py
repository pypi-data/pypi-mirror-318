import numpy as np
import pandas as pd
import geopandas as gpd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# Balanced K-means clustering
def balanced_kmeans(data, num_clusters, tolerance=2, max_iterations=100, optimize_geo=True):
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++')
    kmeans.fit(data)
    centroids = kmeans.cluster_centers_

    clusters = initial_assignment(data, centroids, num_clusters, tolerance)
    labels = np.full(len(data), -1, dtype=int)
    for i, indices in clusters.items():
        for idx in indices:
            labels[idx] = i

    unassigned = set(range(len(data))) - set(idx for indices in clusters.values() for idx in indices)
    for idx in unassigned:
        closest_centroid = np.argmin([np.linalg.norm(data[idx] - centroid) for centroid in centroids])
        clusters[closest_centroid].append(idx)
        labels[idx] = closest_centroid

    # Optimize geographical distribution (optional)
    if optimize_geo:
        clusters = optimize_geographical_distribution(data, clusters)

    return clusters, kmeans, labels


def initial_assignment(data, centroids, num_clusters, tolerance):
    n = len(data)
    base_size = n // num_clusters  # Base size of each cluster
    extra_count = n % num_clusters  # Number of clusters that need one extra data point
    clusters = {i: [] for i in range(num_clusters)}
    distances = np.array([[np.linalg.norm(x - centroids[j]) for j in range(num_clusters)] for x in data])

    assigned = set()
    remaining_indices = set(range(n))
    while remaining_indices:
        for i in range(num_clusters):
            if len(clusters[i]) < base_size + (1 if i < extra_count else 0):
                if not remaining_indices:
                    break
                closest_idx = min(remaining_indices, key=lambda idx: distances[idx, i])
                clusters[i].append(closest_idx)
                assigned.add(closest_idx)
                remaining_indices.remove(closest_idx)

    return clusters


def optimize_geographical_distribution(data, clusters):
    new_clusters = {i: [] for i in clusters}
    cluster_centers = {i: np.mean(data[clusters[i]], axis=0) for i in clusters}

    # Reassign data points to optimize geographical distribution
    for i, points in clusters.items():
        for point in points:
            min_distance = float('inf')
            closest_cluster = i
            for j, center in cluster_centers.items():
                distance = np.linalg.norm(data[point] - center)
                if distance < min_distance:
                    min_distance = distance
                    closest_cluster = j
            new_clusters[closest_cluster].append(point)

    return new_clusters


# Nearest Neighbor 2-opt path planning
def nearest_neighbor_2opt(coords, start_point):
    def calculate_total_distance(route, dist_matrix):
        return sum(dist_matrix[route[i - 1], route[i]] for i in range(len(route)))

    def swap_2opt(route, i, k):
        new_route = np.concatenate((route[0:i], route[k:-len(route) + i - 1:-1], route[k + 1:len(route)]))
        return new_route

    dist_matrix = np.linalg.norm(coords[:, None] - coords, axis=2)
    n = len(coords)
    route = np.arange(n)
    total_distance = calculate_total_distance(route, dist_matrix)

    improvement = True
    while improvement:
        improvement = False
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                new_route = swap_2opt(route, i, k)
                new_distance = calculate_total_distance(new_route, dist_matrix)
                if new_distance < total_distance:
                    route = new_route
                    total_distance = new_distance
                    improvement = True
                    break
            if improvement:
                break

    return np.vstack([start_point, coords[route], start_point])


def path_length(path):
    return np.sum(np.linalg.norm(path[1:] - path[:-1], axis=1))


# Data reading and processing
def read_data(file_path, file_type):
    if file_type == 'xlsx':
        data = pd.read_excel(file_path)
        return data
    elif file_type == 'csv':
        data = pd.read_csv(file_path)
        return data
    elif file_type == 'shp':
        data = gpd.read_file(file_path)
        return data
    else:
        raise ValueError(f"Unsupported file type: {file_type}")


def process_data(file_path, file_type, num_clusters):
    data = read_data(file_path, file_type)
    if file_type == 'shp':
        x, y = data.geometry.x.values, data.geometry.y.values
    else:
        x, y = data.iloc[:, 0].values, data.iloc[:, 1].values

    coords = np.column_stack((x, y))
    clusters, kmeans, labels = balanced_kmeans(coords, num_clusters)
    center_point = np.array([5, 5])
    paths = []
    path_lengths = []
    intra_cluster_ids = []
    for cluster_id, cluster_coords in clusters.items():
        path = nearest_neighbor_2opt(coords[cluster_coords], center_point)
        paths.append(path)
        path_lengths.append(path_length(path))
        intra_cluster_id = np.arange(len(cluster_coords))
        intra_cluster_ids.append(intra_cluster_id)

    centroids = kmeans.cluster_centers_
    cluster_ids = np.zeros(len(x), dtype=int)
    centroid_coords = np.zeros((len(x), 2))
    intra_cluster_id_all = np.zeros(len(x), dtype=int)

    for cluster_id, indices in clusters.items():
        cluster_ids[indices] = cluster_id
        centroid_coords[indices] = centroids[cluster_id]
        intra_cluster_id_all[indices] = intra_cluster_ids[cluster_id]

    data['ClusterID'] = cluster_ids
    data['IntraClusterID'] = intra_cluster_id_all
    data['Centroid_X'] = centroid_coords[:, 0]
    data['Centroid_Y'] = centroid_coords[:, 1]

    return data, paths, path_lengths


# Visualization functions
def visualize_clusters(coords, labels, centers):
    plt.figure(figsize=(12, 6))
    unique_labels = np.unique(labels)
    for label in unique_labels:
        plt.scatter(coords[labels == label, 0], coords[labels == label, 1], label=f'Cluster {label}')
    for i, center in enumerate(centers):
        plt.scatter(center[0], center[1], marker='X', s=200, c='black', label=f'Centroid {i}')
    plt.title('Cluster Visualization')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.show()


def visualize_paths(paths, center_point):
    plt.figure(figsize=(12, 6))
    for path in paths:
        plt.plot(path[:, 0], path[:, 1], marker='o')
    plt.scatter(center_point[0], center_point[1], c='red', marker='x', s=100, label='Center Point')
    plt.title('Path Planning Visualization')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.show()
