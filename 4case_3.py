# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":

      lst = list(map(int, input().split()))

      i_min = lst.index(min(lst))
      lst[-1], lst[i_min] = lst[i_min], lst[-1]
      print(*lst)

