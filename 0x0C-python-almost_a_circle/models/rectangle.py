#!/usr/bin/python3
"""
module for rectangle class
"""
from .base import Base



class Rectangle(Base):
    """This the rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize class instance

        Args:
            width (int): width
            height (int): height
            x (int): x position
            y (int): y position
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """accessor for width property

        Returns: value of the width property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """accessor for width property

        Args:
            value (int): value of the width
 
        Raises:
            TypeError: if value is not an integer
            ValueError: if the value is <= 0
       """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """accessor fo the height property

        Returns: value of the height property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """accessor for the height property

        Args:
            value (int): value of the height property
 
        Raises:
            TypeError: if value is not an integer
            ValueError: if the value is <= 0
       """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """accessor for the x property

        Returns: value of the x position
        """
        return self.__x

    @x.setter
    def x(self, value):
        """accessor for the x property

        Args:
            value (int): value of the x property
  
        Raises:
            TypeError: if value is not an integer
            ValueError: if the value is <= 0
       """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Accessor for the y property

        Returns: value of the y property
        """
        return self.__y

    @y.setter
    def y(self, value):
        """accessor for the y property

        Args:
            value (int): value of the y property
   
        Raises:
            TypeError: if value is not an integer
            ValueError: if the value is < 0
       """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
