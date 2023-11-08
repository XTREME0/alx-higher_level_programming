#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = {key: a_dictionary[key] for key in sorted(a_dictionary)}
    for x, y in a_dictionary.items():
        print("{}: {}".format(x, y))
