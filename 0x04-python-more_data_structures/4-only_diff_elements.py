#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s = []
    for n in set_1:
        if n not in set_2:
            s.append(n)
    for n in set_2:
        if n not in set_1 and n not in s:
            s.append(n)
    return s
