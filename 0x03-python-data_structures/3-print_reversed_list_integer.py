#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    while i:
        i -= 1
        print("{}".format(my_list[i]))