import cmath
import ctypes


class iComplex(ctypes.Structure):
    _fields_ = [("real", ctypes.c_double), ("imag", ctypes.c_double)]

    def __repr__(self):
        imag_sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {imag_sign} {abs(self.imag)}i"

    def __add__(self, other):
        return iComplex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return iComplex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return iComplex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def __pow__(self, other):
        if isinstance(other, iComplex):
            raise NotImplementedError(
                "Exponentiation with another complex number is not supported."
            )

        if isinstance(other, (int, float)):
            result = cmath.exp(other * cmath.log(self.real + self.imag * 1j))
            return iComplex(result.real, result.imag)

        raise TypeError("Exponentiation with non-numeric types is not supported.")

    def __truediv__(self, other):
        if isinstance(other, iComplex):
            denom = other.real**2 + other.imag**2
            if denom == 0:
                raise ZeroDivisionError("Cannot divide by zero complex number.")
            return iComplex(
                (self.real * other.real + self.imag * other.imag) / denom,
                (self.imag * other.real - self.real * other.imag) / denom,
            )
        else:
            return iComplex(self.real / other, self.imag / other)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self == other

    def __pos__(self):
        return self

    def __lt__(self, other):
        return self.real < other.real or (
            self.real == other.real and self.imag < other.imag
        )

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __int__(self):
        return int(self.real)

    def __float__(self):
        return float(self.real)

    def __abs__(self):
        return (self.real**2 + self.imag**2) ** 0.5

    def __neg__(self):
        return iComplex(-self.real, -self.imag)

    def __bool__(self):
        return self.real != 0 or self.imag != 0

    def __hash__(self):
        return hash((self.real, self.imag))
