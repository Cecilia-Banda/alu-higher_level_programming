#!/usr/bin/python3
"""Module defining a 'Rectangle'
"""


class Rectangle():
    """An empty definition of a 'Rectangle'
    """
    width = True
    height = True

    def __init__(self, width=0, height=0):

        """ Instantiates a 'Rectangle'
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ to retrieve it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ to set it
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ to retrieve it
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ to set it
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ that returns the rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """ that returns the perimeter of the rectangle
        """
        if self.width and self.height:
            return (self.width + self.height) * 2
        return 0
