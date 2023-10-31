#!/usr/bin/python3
def uppercase(string):
    buff = ""
    for s in string:
        if ord(s) >= 97 and ord(s) <= 122:
            buff += chr(ord(s) - 32)
        else:
            buff += s
    print("{}".format(buff))
