from unittest import TestCase

from complex import Complex


class TestComplex(TestCase):
    pass

    def test_addition(self):
        z = Complex(1, 2)
        w = Complex(0, 1)

        assert (z + w).__str__() == "1+3i"

    def test_addition_with_real_and_complex_numbers(self):
        z = Complex(1, 2)

        assert (z+5).__str__() == "6+2i"

    def test_addition_with_real_and_complex_numbers_reversed(self):
        z = Complex(1, 2)

        assert (5+z).__str__() == "6+2i"

    def test_addition_resulting_in_negative_imaginary_number(self):
        z = Complex(2, 2)
        w = Complex(1, -3)

        assert (z + w).__str__() == "3-i"

    def test_addition_resulting_in_zero_value_for_real_number(self):
        z = Complex(3, 4)
        w = Complex(-3, 3)

        assert (z + w).__str__() == "7i"

    def test_subtraction(self):
        z = Complex(7, 8)
        w = Complex(6, 7)

        assert (z - w).__str__() == "1+i"

    def test_subtraction_with_real_and_complex_numbers(self):
        z = Complex(4, 4)

        assert (z-2).__str__() == "2+4i"

    def test_subtraction_with_real_and_complex_numbers_reversed(self):
        z = Complex(4, 4)

        assert (2-z).__str__() == "-2-4i"

    def test_subtraction_resulting_in_single_i_value(self):
        z = Complex(6, 7)
        w = Complex(6, 6)

        assert (z - w).__str__() == "i"

    def test_subtraction_resulting_in_both_negative_numbers(self):
        z = Complex(5, 6)
        w = Complex(7, 9)

        assert (z - w).__str__() == "-2-3i"

    def test_conjugate_from_positive_to_negative(self):
        z = Complex(6, 5)

        assert z.conjugate().__str__() == "6-5i"

    def test_conjugate__from_negative_to_positive(self):
        z = Complex(8, -2)

        assert z.conjugate().__str__() == "8+2i"

    def test_conjugate_make_both_numbers_negative(self):
        z = Complex(-9, 4)

        assert z.conjugate().__str__() == "-9-4i"

    def test_modulus(self):
        z = Complex(3, 6)
        number = (int(z.modulus()))

        assert number == 6

    def test_modulus_with_negative_number(self):
        z = Complex(2, -18)
        number = (int(z.modulus()))

        assert number == 18

    def test_modulus_with_both_negative_numbers(self):
        z = Complex(-6, -9)
        number = (int(z.modulus()))

        assert number == 10

    def test_multiply(self):
        z = Complex(2, 5)
        w = Complex(3, 8)

        assert (z * w).__str__() == "-34+31i"

    def test_multiply_all_negative(self):
        z = Complex(-2, -5)
        w = Complex(-3, -8)

        assert (z * w).__str__() == "-34+31i"

    def test_multiply_non_negative_result(self):
        z = Complex(2, -5)
        w = Complex(-3, 8)

        assert (z * w).__str__() == "34+31i"

    def test_equal(self):
        z = Complex(1, 2)
        w = Complex(1, 2)

        assert z == w

    def test_not_equal(self):
        z = Complex(1, 2)
        w = Complex(1, 5)

        assert z != w

    def test_equal_with_negative_numbers(self):
        z = Complex(-1, -2)
        w = Complex(-1, -2)

        assert z == w

    def test_complex_conversion(self):
        z = Complex(5, 8)
        y = complex(5, 8)

        assert z == y

    def test_complex_conversion_with_addition(self):
        assert Complex(2, 3) + (2+2j) == Complex(4, 5)

    def test_complex_conversion_with_int_multiplication(self):
        assert 4*Complex(3, 4) - 2 == Complex(10, 16)
        assert Complex(3, 4)*4 - 2 == Complex(10, 16)
























