#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None or a_dictionary == {}:
        return (None)
    # sort by values and pick highest
    sort_dict = sorted(a_dictionary.items(), key=lambda x: x[1])
    return (sort_dict[-1][0])
