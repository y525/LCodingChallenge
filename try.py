# step 1: preprocess - scaling and standardization
# step 2: choose k
# step 3: select k points randomly as cluster centroids
# step 4: calculate the new centroids/mean
# step 5: repeat until convergence

import numpy as np

class KMeans:
    def __init__(self, k, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations

    def fit(self, X):
        # initialize centroids randomly
        self.m, self.n = np.shape(X)
        self.centroids = X[np.random.choice(range(self.m), self.k)]

        for i in range(self.max_iterations):
            labels = []
            for j in range(self.m):
                distances = np.sqrt(np.sum(np.power(X[j]-self.centroids, 2)))
                labels.append(np.argmin(distances))

            for k in range(self.k):
                points = (labels == k)
                self.centroids[k] = np.mean(points)

            if i > 0 and np.array_equal(self.centroids, previous_centroids):
                break
            previous_centroids = np.copy(self.centroids)
        self.labels = labels

    def predict(self, X):
        labels = []
        for j in range(len(X)):
            distances = np.sqrt(np.sum(np.power(X[j]-self.centroids, 2)))
            labels.append(np.argmin(distances))
        return labels
    

x1 = np.random.randn(5,2) + 5
x2 = np.random.randn(5,2) - 5
X = np.concatenate([x1,x2], axis=0)

# Initialize the KMeans object with k=3
kmeans = KMeans(k=2)

# Fit the k-means model to the dataset
kmeans.fit(X)

# Get the cluster assignments for the input dataset
labels = kmeans.predict(X)

# Print the cluster assignments


# Print the learned centroids
print(kmeans.centroids)


