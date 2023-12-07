#!/usr/bin/env python3

def word_frequencies(filename):
    # Dictionary to hold word frequencies
    freqs = {}

    # Define punctuation to be removed
    punctuation = """!"#$%&'()*,-./:;?@[]_"""

    # Read and process the file
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into words
            words = line.split()

            # Process each word
            for word in words:
                # Remove punctuation from the ends of the word
                cleaned_word = word.strip(punctuation)

                # Count the word
                if cleaned_word:
                    freqs[cleaned_word] = freqs.get(cleaned_word, 0) + 1

    return freqs


# Main function to test word_frequencies
def main():
    filename = "src/alice.txt"
    frequencies = word_frequencies(filename)

    # Print word and its count per line
    for word, count in sorted(frequencies.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
