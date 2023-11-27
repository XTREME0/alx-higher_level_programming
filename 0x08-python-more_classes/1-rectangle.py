#!/usr/bin/python3
""" square module """


class Rectangle:
    """ A rectangle class """

    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """ initiate width and height """

        if width is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if height is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """ width getter """

        return self.__widt

    @property
    def height(self):
        """height getter """

        return self.__height

    @width.setter
    """ width setter """

    def width(self, value):
        if width is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    """ height setter """

    def height(self, value):
        if height is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
