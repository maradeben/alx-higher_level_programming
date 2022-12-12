#!/usr/bin/python3
for i in range(97, 122):
    if (chr(i) == 'q' or chr(i) == 'e'):
        continue
    else:
        print(chr(i), end='')
