#!/usr/bin/python3


sorted_list = []
for name in dir("hidden_4.pyc"):
    if not name.startswith("__"):
        sorted_list.append(name)
sorted_list.sort()
for name in sorted_list:
    print("{:s}".format(name))
