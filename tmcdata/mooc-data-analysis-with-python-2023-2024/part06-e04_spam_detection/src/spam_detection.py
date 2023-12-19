import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import numpy as np


def spam_detection(random_state=0, fraction=1.0):
    # Function to read files
    def read_file(filename, fraction):
        with gzip.open(filename, 'rb') as file:
            lines = file.readlines()
            # Take only a fraction of the lines
            end = int(len(lines) * fraction)
            return [line.decode('utf-8', 'ignore').strip() for line in lines[:end]]

    # Read the data
    ham = read_file('src/ham.txt.gz', fraction)
    spam = read_file('src/spam.txt.gz', fraction)

    # Combine ham and spam emails
    emails = ham + spam
    labels = [0] * len(ham) + [1] * len(spam)

    # Create feature matrix
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(emails)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, labels, train_size=0.75, random_state=random_state)

    # Train the model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate accuracy and number of misclassified points
    acc = accuracy_score(y_test, predictions)
    misclassified = np.sum(predictions != np.array(y_test))

    return acc, len(y_test), misclassified


# Example usage
accuracy, test_size, misclassified = spam_detection(
    random_state=0, fraction=0.1)
print(
    f"Accuracy: {accuracy}, Test size: {test_size}, Misclassified points: {misclassified}")
