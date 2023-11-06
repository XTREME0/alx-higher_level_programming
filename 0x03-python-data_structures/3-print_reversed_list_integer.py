#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    i = len(my_list)
    while i:
        i -= 1
        print("{:d}".format(my_list[i]))
