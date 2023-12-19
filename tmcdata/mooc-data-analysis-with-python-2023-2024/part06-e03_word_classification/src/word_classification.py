#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, KFold

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Load Finnish words from XML file or URL


def load_finnish():
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode('utf-8'))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

# Load English words from a file


def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return lines

# Create a feature matrix based on character frequency


def get_features(words):
    features = np.zeros((len(words), len(alphabet)))
    for i, word in enumerate(words):
        for char in word:
            if char in alphabet:
                features[i, alphabet.index(char)] += 1
    return features

# Check if all characters in a string are in the allowed alphabet


def contains_valid_chars(s):
    return set(s).issubset(alphabet_set)

# Prepare feature matrix and labels for Finnish and English words


def get_features_and_labels():
    finnish_words = [word.lower() for word in load_finnish()
                     if contains_valid_chars(word.lower())]
    english_words = [word.lower() for word in load_english(
    ) if word[0].islower() and contains_valid_chars(word.lower())]

    X = get_features(finnish_words + english_words)
    y = np.array([0] * len(finnish_words) + [1] * len(english_words))
    return X, y

# Perform classification and evaluate using 5-fold cross-validation


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    cv = KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(model, X, y, cv=cv)
    return scores


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()
