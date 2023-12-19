#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy.stats


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = (labels == i)
        # Ignore outlier points
        if np.any(idx):
            new_label = scipy.stats.mode(real_labels[idx])[0][0]
            permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    # Read the data
    df = pd.read_csv('src/data.tsv', sep='\t')
    X = df[['X1', 'X2']]
    y = df['y']

    results = []
    for eps in np.arange(0.05, 0.2, 0.05):
        # Apply DBSCAN clustering
        db = DBSCAN(eps=eps)
        clusters = db.fit_predict(X)

        # Count the number of clusters (ignoring noise/outliers)
        n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
        n_outliers = list(clusters).count(-1)

        # Calculate accuracy if the number of clusters equals the number of labels
        if n_clusters == len(np.unique(y)):
            permutation = find_permutation(n_clusters, y, clusters)
            new_labels = [permutation[label] if label != -
                          1 else -1 for label in clusters]
            # Calculate accuracy only for non-outlier points
            non_outlier_mask = clusters != -1
            score = accuracy_score(y[non_outlier_mask], np.array(
                new_labels)[non_outlier_mask])
        else:
            score = np.nan

        results.append([eps, score, float(n_clusters), float(n_outliers)])

    # Create a DataFrame with the results
    result_df = pd.DataFrame(
        results, columns=['eps', 'Score', 'Clusters', 'Outliers'])
    return result_df


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
