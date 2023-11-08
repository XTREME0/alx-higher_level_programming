#!/bin/usr/python3
def weight_average(my_list=[]):
    if list is None:
        return 0
    x = 0
    y = 0
    for t in my_list:
        x += (t[0] * t[1])
        y += t[1]
    return x / y
