#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    x = 0
    y = 0
    for t in my_list:
        x += (t[0] * t[1])
        y += t[1]
    return (x / y)
