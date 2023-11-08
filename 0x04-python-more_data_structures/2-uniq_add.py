#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    result = 0
    lst = my_list
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            result += lst[i]
    result += lst[i + 1]
    return result
