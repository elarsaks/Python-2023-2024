#!/usr/bin/env python3

def main():
    def triple(n):
        return n * 3

    def square(n):
        return n ** 2

    for i in range(1, 11):
        print(f"triple({i})=={triple(i)} square({i})=={square(i)}")

        if square(i) > triple(i):
            break


if __name__ == "__main__":
    main()
