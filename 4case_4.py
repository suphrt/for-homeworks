# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
  
    lst = list(map(float, input().split()))

    s1 = sum([lst[i] for i in range(len(lst)) if i%2 != 0])
    print(s1, "- cумма элементов списка с нечетными номерами\n")

    s2 = sum(lst[min([i for i in range(len(lst)) if lst[i] < 0]) + 1:max([i for i in range(len(lst)) if lst[i] < 0]):])
    print(s2, "- cумма элементов списка, расположенных между первым и последним отрицательными элементами.\n" )

    s3 = [lst[i] for i in range(len(lst)) if abs(lst[i]) > 1]
    for i in range(len(lst) - len(s3)):
        s3.append(0)
    print(s3, " - сжатый список")
