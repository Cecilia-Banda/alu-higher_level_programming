#!/usr/bin/python3
""" Module defining a 'Rectangle'
"""


class Rectangle():
    """An empty definition of a 'Rectangle'
    """
    width = True
    height = True

    number_of_instances = 0

    def __init__(self, width=0, height=0):

        """ Instantiates a 'Rectangle'
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):

        """Sets the print behavior of the Rectangle object.
        """
        if self.height and self.width:
            return '\n'.join(["#" * self.width] * self.height)
        return ""

    def __repr__(self):
        """Sets the repr behavior of the Rectangle object.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Sets the del behavior of the Rectangle object.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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
