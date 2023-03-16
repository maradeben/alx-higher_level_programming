#!/usr/bin/python3

def best_score(a_dictionary):

    try:
        # sort by values and pick highest
        sort_dict = sorted(a_dictionary.items(), key=lambda x: x[1])
        return (sort_dict[-1][0])
    except (AttributeError, KeyError):
        return (None)
