#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw = {key: (value * 2) for key, value in a_dictionary.items()}
    return nw
