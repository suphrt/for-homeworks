# !/usr/bin/env python 3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":

    lst = list(map(float, input('Введите элементы списка\n').split()))
    
    print(max(lst), "- максимальный элемент списка.\n")

    l = len(lst)

    summa = sum(lst[:max([i for i in range(l) if lst[i] > 0]):])
    print(summa, '- сумма элементов списка, расположенных до последнего положительного элемента.\n')

    a = float(input('Введите а\n'))
    b = float(input('Введите b\n'))

    compr = [lst[i] for i in range(l) if abs(lst[i]) < a or abs(lst[i]) > b]
    for i in range(l - len(compr)):
        compr.append(0)
    print(compr, "- сжатый список.\n")
