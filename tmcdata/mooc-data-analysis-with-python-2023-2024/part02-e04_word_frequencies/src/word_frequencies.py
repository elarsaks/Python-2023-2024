#!/usr/bin/env python3

def word_frequencies(filename):
    result = {}
    with open(filename) as in_file:
        for w in in_file.read().split():
            ws = w.strip("""!"#$%&'()*,-./:;?@[]_""")
            if ws not in result:
                result[ws] = 0
            result[ws] += 1
    return result


def main():
    for word, count in word_frequencies("src/alice.txt").items():
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
