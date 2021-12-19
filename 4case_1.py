# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":

      lst = list(map(int, input().split()))

      i_max = lst.index(max(lst))
      lst[i_max], lst[0] = lst[0], lst[i_max]
      print(*lst)

