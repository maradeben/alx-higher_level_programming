#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = number % 10

# this is to get around Pythn's modulo behavior
if number < 0:
    abs = number * -1
    rem = -(abs % 10)

if rem > 5:
    extra = "greater than 5"
elif rem == 0:
    extra = "0"
elif rem < 6:
    extra = "less than 6 and not 0"
print(f"Last digit of {number} is {rem} and is {extra}")
