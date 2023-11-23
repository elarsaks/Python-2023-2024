#!/usr/bin/env python3


def acronyms(s):
    # Importing the string module for punctuation
    import string

    # Split the string into words
    words = s.split()

    # Function to remove punctuation from a word
    def remove_punctuation(word):
        return ''.join(char for char in word if char not in string.punctuation)

    # Extract acronyms: words with length >= 2 and all characters in uppercase
    acronyms = [remove_punctuation(word) for word in words if len(
        word) >= 2 and word.isupper()]

    return acronyms


def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
