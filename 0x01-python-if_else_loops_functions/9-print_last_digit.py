#!/usr/bin/python3
def print_last_digit(number):
    if not isinstance(number, int):
        return ''
    print("{}".format(str(number)[-1]), end='')
    return str(number)[-1]
