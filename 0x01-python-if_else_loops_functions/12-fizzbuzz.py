#!/usr/bin/python3
"""
Print 1 through 100
print 'Fizz' for multiples of 3
print 'Buzz' for multiples of 5
print 'FizzBuzz' for number that are multiples of both
"""


def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')
