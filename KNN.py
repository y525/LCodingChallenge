import numpy as np

class KNN:
    def __init__(self, k):
        self.k = k
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    def predict(self, X):
        y_pred = np.zeros(X.shape[0])

        for i, x_test in enumerate(X):
            
