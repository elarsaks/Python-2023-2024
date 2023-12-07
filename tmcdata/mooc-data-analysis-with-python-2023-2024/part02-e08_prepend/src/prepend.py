#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, start):
        self.start = start

    def write(self, text):
        print(self.start + text)


def main():
    p = Prepend("+++ ")
    p.write("Hello")
    pass


if __name__ == "__main__":
    main()
