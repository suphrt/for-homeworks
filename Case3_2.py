#!/usr/bin/env python3

n = int(input("Enter number \n"))
c500 = 0
c100 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0

while n >= 500:
    n = n - 500
    c500 = c500 + 1
while n >= 100:
    n = n - 100
    c100 = c100 + 1
while n >= 10:
    n = n - 10
    c10 = c10 + 1
while n >= 5:
    n = n - 5
    c5 = c5 + 1
while n >= 2:
    n = n - 2
    c2 = c2 + 1
while n >= 1:
    n = n - 1
    c1 = c1 + 1
print(" 500", "-", c500, '\n', "100", "-", c100, '\n', "10", "-", c10, '\n',  "5", "-", c5, '\n', "2", "-", c2, '\n', "1", "-", c1)
