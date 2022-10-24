"""
Module to create fractions. Supports simple math operations and comparison
"""


class FractionError(BaseException):
    """
    A class to check an object if it is a fraction type
    """


class FractionZeroError(BaseException):
    """
    A class to check if there no zeroes in fraction object attributes
    """


class Fraction:
    """
    A class to create and operate with fractions
    ----------
    Atributes:
    self.n: int
        numerator
    self.d: int
        denominator
    ----------
    Methods:
    reduction(numerator: int, denominator: int):
        static method, for reducing fractions
    common_denominator(d_self:int, d_other:int):
        static method, to determine the common denominator
    """

    def __init__(self, numerator: int, denominator: int):
        try:
            if numerator > 0 and denominator > 0:
                self.num = numerator
                self.den = denominator
            else:
                raise FractionZeroError
        except FractionZeroError:
            print("Not numerator nor denominator can't be equal to zero")

    def __str__(self):
        return f"({self.num}/{self.den})"

    @staticmethod
    def reduction(numerator: int, denominator: int):
        """
        To reduce fractions for better math. If both numerator
        and denomimator are divisible without a remainder for
        number in range equal min(numerator, denomimator), both
        will be divided by this number
        """
        if numerator > denominator:
            number = denominator
        else:
            number = numerator
        while number > 1:
            if numerator % number == 0 and denominator % number == 0:
                numerator //= number
                denominator //= number
            else:
                number -= 1
        return numerator, denominator

    @staticmethod
    def common_denominator(d_self: int, d_other: int):
        """
        To find a common denominator for the most operations
        with fractions, we search for the number wich is floor
        divisible on both numerator and denomimator
        """
        for num in range(max(d_self, d_other), (d_self * d_other + 1)):
            if num % d_self == 0 and num % d_other == 0:
                return num

    def __mul__(self, other):
        try:
            if isinstance(other, Fraction):
                result = self.reduction(self.num * other.num, self.den * other.d)
                return Fraction(result[0], result[1])
            else:
                raise FractionError
        except FractionError:
            return "You must operate with fractions only"

    def __truediv__(self, other):
        try:
            if isinstance(other, Fraction):
                result = self.reduction(self.num * other.d, self.den * other.num)
                return Fraction(result[0], result[1])
            else:
                raise FractionError
        except FractionError:
            return "You must operate with fractions only"

    def __add__(self, other):
        try:
            if isinstance(other, Fraction):
                denomimator = self.common_denominator(self.den, other.d)
                self_num_index = int(denomimator / self.den)
                other_num_index = int(denomimator / other.d)
                numerator = self.num * self_num_index + other.num * other_num_index
                result = self.reduction(numerator, denomimator)
                return Fraction(result[0], result[1])
            else:
                raise FractionError
        except FractionError:
            return "You must operate with fractions only"

    def __sub__(self, other):
        try:
            if isinstance(other, Fraction):
                denomimator = self.common_denominator(self.den, other.d)
                self_num_index = int(denomimator / self.den)
                other_num_index = int(denomimator / other.d)
                numerator = self.num * self_num_index - other.num * other_num_index
                result = self.reduction(numerator, denomimator)
                return Fraction(result[0], result[1])
            else:
                raise FractionError
        except FractionError:
            return "You must operate with fractions only"

    def __gt__(self, other):
        try:
            if isinstance(other, Fraction):
                denomimator = self.common_denominator(self.den, other.den)
                self_num_to_compare = self.num * int(denomimator / self.den)
                other_num_to_compare = other.num * int(denomimator / other.den)
                return self_num_to_compare > other_num_to_compare
            else:
                raise FractionError
        except FractionError:
            return "You must operate with fractions only"

    def __lt__(self, other):
        try:
            if isinstance(other, Fraction):
                denomimator = self.common_denominator(self.den, other.den)
                self_num_to_compare = self.num * int(denomimator / self.den)
                other_num_to_compare = other.num * int(denomimator / other.den)
                return self_num_to_compare < other_num_to_compare
            else:
                raise FractionError
        except FractionError:
            return "You must operate with fractions only"

    def __ne__(self, other):
        try:
            if isinstance(other, Fraction):
                denomimator = self.common_denominator(self.den, other.den)
                self_num_to_compare = self.num * int(denomimator / self.den)
                other_num_to_compare = other.num * int(denomimator / other.den)
                return self_num_to_compare != other_num_to_compare
            else:
                raise FractionError
        except FractionError:
            return "You must operate with fractions only"

    def __eq__(self, other):
        try:
            if isinstance(other, Fraction):
                denomimator = self.common_denominator(self.den, other.den)
                self_num_to_compare = self.num * int(denomimator / self.den)
                other_num_to_compare = other.num * int(denomimator / other.den)
                return self_num_to_compare == other_num_to_compare
            else:
                raise FractionError
        except FractionError:
            return "You must operate with fractions only"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    m = 5
    print(x + y == Fraction(3, 4))
    print(x == y)
    print(x * y)
    print(x * m)
