#!/usr/bin/python3
""" define a square class """


class Square:
    """ square class """


    __size = None
    size = None

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ return square area """

        return pow(self.__size, 2)

    @property
    def size(self):
        """ size getter """

        return self.__size
    @size.setter
    def size(self, size):
        """ size setter """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
