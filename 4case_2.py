# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

from math import prod

if __name__ == "__main__":

      lst = list(map(int, input().split()))
      lst = prod([int(a) for a in lst if a > 0])
      print(lst)
