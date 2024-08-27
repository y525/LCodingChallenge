# step 1: preprocess - scaling and standardization
# step 2: choose k
# step 3: select k points randomly as cluster centroids
# step 4: calculate the new centroids/mean
# step 5: repeat until convergence

import numpy as np

def initialize_random_centroids(K, X):
    m, n  = np.shape(X)
    centroids = np.empty((K, n))
    for i in range(K):
        centroids[i] = X[np.random.choice(range(m))]
    return centroids

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum(np.power(x1-x2, 2))) # np.linalg.norm(x1, x2)

def closest_centroid(x, centroids, K):
    distances = np.empty(K)
    for i in range(K):
        distances[i] = euclidean_distance(centroids[i], x)
    return np.argmin(distances)

def create_clusters(centroids, K, X):
    m, _ = np.shape(X)
    cluster_idx = np.empty(m)
    for i in range(m):
        cluster_idx[i] = closest_centroid(X[i], centroids, K)
    return cluster_idx

def compute_means(cluster_idx, K, X):
    _, n = np.shape(X)
    centroids = np.empty((K, n))
    for i in range(K):
        points = X[cluster_idx == i]
        centroids[i] = np.mean(points, axis=0)
    return centroids

def run_Kmeans(K, X, max_iterations=500):
    centroids = initialize_random_centroids(K, X)
    print(f"initial centroids: {centroids}")
    for _ in range(max_iterations):
        clusters = create_clusters(centroids, K, X)
        previous_centroids = centroids
        centroids = compute_means(clusters, K, X)
        diff = previous_centroids-centroids
        if not diff.any():
            return clusters
    return clusters

x1 = np.random.randn(5,2) + 5
x2 = np.random.randn(5,2) - 5
X = np.concatenate([x1,x2])
kmeans = run_Kmeans(2, X, 100)
print(kmeans)
print(X)
print(x1)








