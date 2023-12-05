#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as file:
        for l in file:
            print(l, end="")
    file.close
