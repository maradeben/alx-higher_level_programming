#!/usr/bin/python3

for i in range(0, 9):
    for j in range(1, 10):
        print("{:d}{:d}".format(i, j), end='')
        if not (i == 8 and j == 9):
            print(end=", ")
print('')
