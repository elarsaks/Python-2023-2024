#!/usr/bin/env python3

def reverse_dictionary(d):
    reversed_dict = {}
    for eng_word, finn_words in d.items():
        for finn_word in finn_words:
            # If the Finnish word is already a key in the reversed dictionary,
            # append the current English word to its list.
            if finn_word in reversed_dict:
                reversed_dict[finn_word].append(eng_word)
            else:
                # Otherwise, create a new entry with the Finnish word as the key
                # and a list containing the current English word.
                reversed_dict[finn_word] = [eng_word]
    return reversed_dict


def main():
    pass


if __name__ == "__main__":
    main()
