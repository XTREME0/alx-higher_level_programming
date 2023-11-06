#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = [num % 2 - 1 for num in my_list]
    return lst
