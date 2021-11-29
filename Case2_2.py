# !/usr/bin/env python3

if __name__ == "__main__":

    n = int(input())

    if 5 < n < 14:
        print(n)
    elif n == 14:
        print(17)
    else:
        print("Card with this value does not exist")
