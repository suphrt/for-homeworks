#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = float(input("a?\n"))
    b = float(input("b?\n"))
    c = float(input("c?\n"))
    x = float(input("x?\n"))
    y = float(input("y?\n"))

    s = x * y

    if (a * c) <= s or (a * b) <= c or (b * c) <= s:
        print("Кирпич пройдёт")
    else:
        print("Кирпич не пройдёт")