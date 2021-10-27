#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

if __name__ == "__main__":

    a = float(input("a? \n"))

    if a == 0:
        print("a can't be zero.")
    else:
        b = float(input("b? \n"))
        c = float(input("c? \n"))

        D = b * b - 4 * a * c

        if D > 0:
            x1 = (-b - sqrt(D)) / (2 * a)
            x2 = (-b + sqrt(D)) / (2 * a)
            if x1 != x2:
                print(x1 , x2)
            else:
                print("Both roots are equal and their value is", x1)
        elif D == 0:
            x = -b / (2 * a)
            print(x)
        else:
            print("No roots.")
