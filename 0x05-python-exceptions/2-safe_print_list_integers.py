#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while x > 0:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            x -= 1
        except ValueError:
            i += 1
            x -= 1
    print("")
    return i
