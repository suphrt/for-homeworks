# !/usr/bin/env python3

if __name__ == "__main__":

    k = int(input())
    d = 0
    if k % 7 == 0:
        print("Sun")
    elif k <= 7:
        d = k
    elif k % 7 != 0:
        d = k % 7
    else:
        d = k / 7
    if d == 1:
        print("Monday")
    elif d == 2:
        print("Tuesday")
    elif d == 3:
        print("Wednesday")
    elif d == 4:
        print("Thursday")
    elif d == 5:
        print("Friday")
    elif d == 6:
        print("Saturday")