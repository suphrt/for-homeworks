#!/usr/bin/env python3

if __name__ == "__main__":

    n = int(input("Enter number \n"))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i, "*", j, "=", i * j)
