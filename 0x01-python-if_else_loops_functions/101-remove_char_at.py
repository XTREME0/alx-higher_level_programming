#!/usr/bin/python3
def remove_char_at(str, n):
    y = ""
    j = -1
    for i in str:
        j += 1
        if j == n:
            continue
        y += i

    return y
