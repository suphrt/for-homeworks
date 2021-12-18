# !/usr/bin/env python3

if __name__ == "__main__":

    n = int(input())

    if 0 <= n <= 11:
        month = n + 1
        if month == 1:
            print("January")
        elif month == 2:
            print("February")
        elif month == 3:
            print("March")
        elif month == 4:
            print("April")
        elif month == 5:
            print("May")
        elif month == 6:
            print("June")
        elif month == 7:
            print("July")
        elif month == 8:
            print("August")
        elif month == 9:
            print("September")
        elif month == 10:
            print("October")
        elif month == 11:
            print("November")
        else:
            print("December")
    else:
        print("Month with this number does not exist")
