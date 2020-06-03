#!/usr/bin/env python
import math


class Complex:

    def __init__(self, real, imag=0):
        """
        Constructor initializing Complex obj with default value for imag
        :param real: no default value
        :param imag: default value of 0
        """
        self.real = real
        self.imag = imag

    def conjugate(self):
        """
        Flips operator to opposite value
        :return: new Complex obj with modified values
        """
        i = self.imag * -1

        return Complex(self.real, i)

    def modulus(self):
        """
        Calculates the “length” of the number when we consider it as a point in the complex plane
        :return: length value of Complex obj
        """
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __add__(self, other):
        """
        Adds two Complex obj. This example has function to add Complex numbers with integers
        :param other: second Complex obj
        :return: new Complex obj with modified values
        """
        if isinstance(other, (float, int)):
            other = Complex(other)
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """
        Subtracts two Complex obj. This example has function to subtract Complex numbers with integers
        :param other: second Complex obj
        :return: new Complex obj with modified values
        """
        if isinstance(other, (float, int)):
            other = Complex(other)
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """
        Multiplies two Complex obj. This example has function to multiply Complex numbers with integers
        :param other: second Complex obj
        :return: new Complex obj with modified values
        """
        if isinstance(other, (float, int)):
            other = Complex(other)

        r = (self.real * other.real) - (self.imag * other.imag)
        i = (self.real * other.imag) + (other.real * self.imag)
        return Complex(r, i)

    def __eq__(self, other):
        """
        Checks if two Complex obj are equal.
        :param other: second Complex obj
        :return: boolean value
        """
        return self.real == other.real and self.imag == other.imag

    def __radd__(self, other):
        """
        Reverse add, gives opportunity to choose order of addition
        :param other: second Complex obj
        :return: call to add function
        """
        return self.__add__(other)

    def __rsub__(self, other):
        """
        Reverse sub, gives opportunity to choose order of subtraction
        :param other: second Complex obj
        :return: call to sub function
        """
        if isinstance(other, (float, int)):
            other = Complex(other)
        return other.__sub__(self)

    def __rmul__(self, other):
        """
        Reverse mul, gives opportunity to choose order of multiplication
        :param other: second Complex obj
        :return: call to mul function
        """
        return self.__mul__(other)

    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        return Complex(-self.real, -self.imag)

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        return complex(self.real, self.imag)

    def __str__(self):
        """
        To string method with checks for different values
        :return: string with correct format based on value of Complex number
        """
        if self.imag > 0:
            if self.imag == 1 and self.real == 0:
                return "i"
            elif self.real == 0:
                return f"{self.imag}i"
            elif self.imag == 1:
                return f"{self.real}+i"
            else:
                return f"{self.real}+{self.imag}i"
        elif self.imag < 0:
            if self.imag == -1:
                return f"{self.real}-i"
            else:
                return f"{self.real}{self.imag}i"
        elif self.imag == 0:
            return f"{self.real}"
