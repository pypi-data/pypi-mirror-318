import numpy as np
import pandas as pd
import geopandas as gpd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Balanced clustering
import numpy as np
from sklearn.cluster import KMeans


def balanced_cluster(data, num_clusters, tolerance=2, max_iterations=100, optimize_geo=True):
    balanced_model = KMeans(n_clusters=num_clusters, init='k-means++')
    balanced_model.fit(data)
    centroids = balanced_model.cluster_centers_

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
        clusters = optimize_geographical_distribution_with_trade(data, clusters, centroids)

    # Count the number of data in each cluster
    cluster_sizes = {i: len(indices) for i, indices in clusters.items()}

    return clusters, balanced_model, labels, cluster_sizes


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



def optimize_geographical_distribution_with_trade(data, clusters, centroids):
    new_clusters = clusters.copy()
    cluster_centers = {i: np.mean(data[clusters[i]], axis=0) for i in clusters}

    # Trade points to maintain balance
    while True:
        balanced = True
        for i in range(len(new_clusters)):
            for j in range(i + 1, len(new_clusters)):
                size_diff = abs(len(new_clusters[i]) - len(new_clusters[j]))
                if size_diff > 1:  # Check if clusters are imbalanced
                    balanced = False
                    if len(new_clusters[i]) > len(new_clusters[j]):
                        larger_cluster, smaller_cluster = i, j
                    else:
                        larger_cluster, smaller_cluster = j, i

                    # Find the point in the larger cluster that is closest to the centroid of the smaller cluster
                    closest_point = min(new_clusters[larger_cluster], key=lambda point: np.linalg.norm(data[point] - cluster_centers[smaller_cluster]))
                    new_clusters[larger_cluster].remove(closest_point)
                    new_clusters[smaller_cluster].append(closest_point)
                    break
            if not balanced:
                break
        if balanced:
            break

    return new_clusters


# Nearest Neighbor 2-opt path planning
def nearest_neighbor_2opt(coords, start_point):
    def calculate_total_distance(route, dist_matrix):
        return sum(dist_matrix[route[i - 1], route[i]] for i in range(len(route)))

    def swap_2opt(route, i, k):
        new_route = np.concatenate((route[0:i], route[k:-len(route) + i - 1:-1], route[k + 1:len(route)]))
        return new_route

    # Add start_point to coords
    coords = np.vstack([start_point, coords])
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

    # Ensure the route starts and ends at start_point
    if route[0] != 0:
        route = np.roll(route, -np.where(route == 0)[0][0])
    if route[-1] != 0:
        route = np.append(route, 0)

    return coords[route]


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
    clusters, balanced_model, labels = balanced_cluster(coords, num_clusters)
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

    centroids = balanced_model.cluster_centers_
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
    plt.figure(figsize=(14, 8))
    unique_labels = np.unique(labels)
    # Plot each cluster's data points
    for label in unique_labels:
        plt.scatter(coords[labels == label, 0], coords[labels == label, 1], label=f'Cluster {label}')

    plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=200, c='black', label='Centroid')

    plt.title('Cluster Visualization')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()

    # Adjust axis limits to leave space for legend
    plt.xlim(coords[:, 0].min() - 1, coords[:, 0].max() + 1)
    plt.ylim(coords[:, 1].min() - 1, coords[:, 1].max() + 1)

    plt.show()


def visualize_paths(paths, center_point):
    plt.figure(figsize=(14, 8))  # Increase the figure size for better visibility
    for i, path in enumerate(paths):
        plt.plot(path[:, 0], path[:, 1], marker='o', label=f'Path {i}')

    plt.scatter(center_point[0], center_point[1], c='red', marker='x', s=100, label='Center Point')

    plt.title('Path Planning Visualization')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()

    all_coords = np.vstack(paths)
    plt.xlim(all_coords[:, 0].min() - 1, all_coords[:, 0].max() + 1)
    plt.ylim(all_coords[:, 1].min() - 1, all_coords[:, 1].max() + 1)

    plt.show()
