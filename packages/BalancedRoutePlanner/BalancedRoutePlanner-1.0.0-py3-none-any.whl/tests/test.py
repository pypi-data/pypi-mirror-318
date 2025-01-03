import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from BalancedRoutePlanner import balanced_cluster, nearest_neighbor_2opt, path_length, visualize_clusters, visualize_paths
import numpy as np
import pandas as pd

# Generate synthetic test data
def generate_data(n_samples, x_range, y_range):
    x = np.random.uniform(x_range[0], x_range[1], n_samples)
    y = np.random.uniform(y_range[0], y_range[1], n_samples)
    return x, y

# Define input parameters
test_sizes = [50, 151, 300, 201]
cluster_numbers = [3, 6, 5, 2]

# Process and visualize each test case
for size, num_clusters in zip(test_sizes, cluster_numbers):
    x, y = generate_data(size, [0, 10], [0, 10])
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

    data = pd.DataFrame({
        'X_coordinate': x,
        'Y_coordinate': y,
        'ClusterID': cluster_ids,
        'IntraClusterID': intra_cluster_id_all,
        'Centroid_X': centroid_coords[:, 0],
        'Centroid_Y': centroid_coords[:, 1]
    })

    # Print data
    print(f"Data for size {size} and {num_clusters} clusters:")
    print(data.head())

    # Visualize results
    visualize_clusters(coords, labels, centroids)
    visualize_paths(paths, center_point)

print("Testing complete.")
