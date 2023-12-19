#!/usr/bin/env python3

import scipy
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import numpy as np


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def plant_clustering():
    # Load the iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Apply k-means clustering
    kmeans = KMeans(n_clusters=3, random_state=0)
    clusters = kmeans.fit_predict(X)

    # Find the best permutation of cluster labels
    permutation = find_permutation(3, y, clusters)
    new_labels = [permutation[label] for label in clusters]

    # Calculate and return the accuracy score
    return accuracy_score(y, new_labels)


def main():
    accuracy = plant_clustering()
    print(f"Accuracy is {accuracy}")


if __name__ == "__main__":
    main()
