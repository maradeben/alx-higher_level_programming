#!/usr/bin/python3
import random
number = random.randint(-10, 10)
status = 'null'
if number < 0:
    status = 'negative'
elif number > 0:
    status = 'positive'
elif number == 0:
    status = 'zero'

print(f"{number} is {status}")
