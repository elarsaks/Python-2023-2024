import sys


def file_count(filename):
    lines_count = 0
    words_count = 0
    chars_count = 0

    with open(filename, 'r') as file:
        for line in file:
            lines_count += 1
            words_count += len(line.split())
            chars_count += len(line)

    return lines_count, words_count, chars_count


def main():
    for filename in sys.argv[1:]:
        line_count, word_count, char_count = file_count(filename)
        print(f"{line_count}\t{word_count}\t{char_count}\t{filename}")


if __name__ == "__main__":
    main()
