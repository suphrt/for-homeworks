# !/usr/bin/env python3

if __name__ == "__main__":

    n = int(input())

    if 0 <= n <= 11:
        month = n + 1
        if month == 1:
            print("Jan")
        elif month == 2:
            print("Feb")
        elif month == 3:
            print("Mar")
        elif month == 4:
            print("Apr")
        elif month == 5:
            print("May")
        elif month == 6:
            print("Jun")
        elif month == 7:
            print("Jul")
        elif month == 8:
            print("Aug")
        elif month == 9:
            print("Sep")
        elif month == 10:
            print("Oct")
        elif month == 11:
            print("Nov")
        else:
            print("Dec")
    else:
        print("Error")