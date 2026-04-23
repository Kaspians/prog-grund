def GCD(a: int, b: int) -> int:
    """
    Greatest common Divisor

    Always return *postive int*, because of `abs(a)`
    """

    while True:
        t = b
        b = a % b
        a = t
        if b == 0:
            break
    return abs(a)


# def numerDenom(p1: int, p2: int) -> tuple[int, int]:
#     """
#     Return a tuple of two integers,
#     * t[0] = *täljaren*
#     * t[1] = *nämnaren*
#     """
#     return (int(p1 / GCD(p1, p2)), int(p2 / GCD(p1, p2)))


class Frac:
    """Straight up *Frac*s"""

    def __init__(self, a: int, b: int):
        """
        # Upg2 + Upg3
        *Isgood, innit? Wus's in-it?*

        `numer` is GCD of *täljaren*
        `denom` is GCD of *nämnaren*
        """
        self.a = a
        self.b = b
        self.numer = int(a / GCD(a, b))
        self.denom = int(b / GCD(a, b))

    def __str__(self) -> str:
        """
        # Upg3
        **Pro-Fortnite tip**:
        When the *class* is called (`Frac`) with `str()` or `print()`,
        `__str__` is automatically returned
        """
        n = self.numer
        d = self.denom
        return f'{n}/{d}'

    def add(self, other: 'Frac') -> 'Frac':
        """
        *Addify* `a+b`

        a, b = *self*.a,b
        c, d = *other*.a, b
        a   c   ad + bc
        — + — = ————————
        b   d      bd
        """
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        num = a * d + b * c
        dem = b * d
        return Frac(num, dem)

    def sub(self, other: 'Frac') -> 'Frac':
        """
        *Subify*: `a-b`

        a, b = *self*.a,b
        c, d = *other*.a, b
        a   c   ad - bc
        — - — = ————————
        b   d      bd
        """
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        num = a * d - b * c
        dem = b * d
        return Frac(num, dem)

    def mul(self, other: 'Frac') -> 'Frac':
        """
        *Multiply*: `a*b`

        a, b = *self*.a,b
        c, d = *other*.a, b
        a   c   ac
        — * — = ——
        b   d   bd
        """
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        num = a * c
        dem = b * d
        return Frac(num, dem)

    def div(self, other: 'Frac') -> 'Frac':
        """
        *Divify*: `a/b`

        a, b = *self*.a,b
        c, d = *other*.a, b
        a/b   ad
        ——— = ——
        c/d   bc
        """
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        num = a * d
        dem = b * c
        return Frac(num, dem)

    def __add__(term1: 'Frac', term2: 'Frac') -> 'Frac':
        return Frac.add(term1, term2)

    def __sub__(term1: 'Frac', term2: 'Frac') -> 'Frac':
        return Frac.sub(term1, term2)

    def __mul__(prod1: 'Frac', prod2: 'Frac') -> 'Frac':
        return Frac.mul(prod1, prod2)

    def __truediv__(num: 'Frac', dem: 'Frac') -> 'Frac':
        return Frac.div(num, dem)
