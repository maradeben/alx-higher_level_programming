#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = [i for i in my_list]
    new_list = [replace if new_list[i] == search else i
                for i in range(len(new_list))]
    return (new_list)
