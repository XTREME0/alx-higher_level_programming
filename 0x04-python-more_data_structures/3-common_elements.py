#!/usr/bin/python3
def common_elements(set_1, set_2):
    s = []
    for n in set_1:
        if n in set_2:
            s.append(n)
    return s
