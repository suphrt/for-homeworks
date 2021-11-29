#!usr/bin/env python3

from math import sqrt

n = int(input("Enter number \n"))

if n < 2:
    print("The number must be more than 1")
    quit()
elif n == 2:
    print("1")
    quit()

i = 2

k = int(sqrt(n))

while i <= k:
    if n % i == 0:
        print("0")
        quit()
    i += 1
print("1")
