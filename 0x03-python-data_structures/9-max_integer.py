#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxx = my_list[0]
    for num in my_list:
        maxx = num if num > maxx else maxx
    return maxx
