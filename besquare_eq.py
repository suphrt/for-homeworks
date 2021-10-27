#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

if __name__ == "__main__":
    a = float(input("a?\n "))
    if a == 0:
        print("a can't be zero.")
    else:
        b = float(input("b?\n "))
        c = float(input("c?\n "))

        D = b * b - 4 * a * c

        if D > 0:
            t1 = (-b - sqrt(D)) / (2 * a)
            t2 = (-b + sqrt(D)) / (2 * a)
            if t1 != t2:
                print(-sqrt(t1), sqrt(t1), -sqrt(t2), sqrt(t2))
            else:
                print("Some roots are equal and their value is ", -sqrt(t1), sqrt(t1))
        elif D == 0:
            t = -b / (2 * a)
            print(-sqrt(t), sqrt(t))
        else:
            print("No roots.")
