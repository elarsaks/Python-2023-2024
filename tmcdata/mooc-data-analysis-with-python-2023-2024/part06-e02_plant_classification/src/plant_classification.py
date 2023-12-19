#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


def plant_classification():
    # Load the iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)

    # Initialize Gaussian Naive Bayes classifier
    gnb = GaussianNB()

    # Fit the classifier to the training data
    gnb.fit(X_train, y_train)

    # Predict the labels of the test set
    y_pred = gnb.predict(X_test)

    # Calculate and return the accuracy score
    return accuracy_score(y_test, y_pred)


def main():
    accuracy = plant_classification()
    print(f"Accuracy is {accuracy}")


if __name__ == "__main__":
    main()
