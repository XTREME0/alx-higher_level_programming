#!/usr/bin/python3
""" define a square class """


class Square:
    """ square class """

    __size = None
    __position = None
    size = None

    def __init__(self, size=0, position=(0, 0)):
        if len(position) != 2 or not all(isinstance(p, int) for p in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        self.__position = position

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

    def my_print(self):
        if self.__position and self.__size:
            for x in range(self.__position[1]):
                print("")
        for i in range(self.__size):
            if self.__position:
                print(" "*self.__position[0], end="")
            print("#"*self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
