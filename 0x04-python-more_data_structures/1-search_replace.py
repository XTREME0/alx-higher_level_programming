#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lst = []
    for s in my_list:
        if s == search:
            lst.append(replace)
        else:
            lst.append(s)
    return lst
