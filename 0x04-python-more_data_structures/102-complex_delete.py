#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete = []
    for key, val in a_dictionary.items():
        if val == value:
            to_delete.append(key)
    for i in to_delete:
        del a_dictionary[i]
    return a_dictionary
