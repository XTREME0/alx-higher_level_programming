#!/usr/bin/python3

""" read_file function """

def read_file(filename=""):
    """ 
    function to read a file and print it 
    Args:
        filename: filename duuh
    """

    with open(filename, 'r') as file:
        for l in file:
            print(l, end="")
    file.close
