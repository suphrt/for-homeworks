#!usr/bin/env python3
# -*- coding: utf-8 -*-

w = 5   # number of words
d = 2   # number of new words
t = 1   # the first day
s = 10  # number of days

while t < s:
    w += d
    t += 1
print("Количество слов выученных в", s, "день составляет", w)
