#!usr/bin/env python

n = 64
g = 2
r = 4

for i in range(64):
    for j in range(64):
        if i * g + j * r == 64:
            print ("Number of geese -", i, '\n' "Number of rabbits -", j, '\n')