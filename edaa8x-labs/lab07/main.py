#!/usr/bin/env python3

from frac import GCD
from frac import Frac


def main() -> None:
    """
    A *while loop* creating an interacting session.
    Input the `n` of the *upg{`n`}* you want to *print()*.
    * 1. GCD
    * 2. Frac.numer/denom
    * 3. Frac.__str__
    * 4. Frac.add()/sub()/mul()/div()
    * 5. sum (CLEAN)
    * 6. Frac.__add__/__sub__/__mul__/__truediv__
    """
    while True:
        ask = input('Which upg[n] do you want?: ')

        if ask == '1':
            g = GCD(int(input('a')), int(input('b')))
            print('GCD =', g)

        elif ask == '2':
            x = Frac(3, 9)
            print(x.numer, x.denom)

        elif ask == '3':
            x = Frac(3, 9)
            print(x)

        elif ask == '4':
            # add
            x = Frac(1, 6)
            y = Frac(1, 6)
            z = x.add(y)
            print(f'{x} + {y} = {z}')  # Skriver ut 1/6 + 1/6 = 1/3
            # sub
            x = Frac(2, 3)
            y = Frac(1, 6)
            z = x.sub(y)
            print(f'{x} - {y} = {z}')  # Skriver ut 2/3 - 1/6 = 1/2
            # mul
            x = Frac(2, 5)
            y = Frac(3, 4)
            z = x.mul(y)
            print(f'{x} * {y} = {z}')  # Skriver ut 2/5 * 3/4 = 3/10
            # div
            x = Frac(3, 7)
            y = Frac(5, 2)
            z = x.div(y)
            print(f'{x} / {y} = {z}')  # Skriver ut 3/7 / 5/2 = 6/35

        elif ask == '5':
            a = Frac(1, 3)
            b = Frac(1, 3)
            c = Frac(1, 6)
            d = Frac(1, 6)
            sum = a.add(b.add(c.mul(d)))  # CLEAN!
            print(f'{sum}')

        elif ask == '6':
            x = Frac(2, 3)
            y = Frac(1, 4)
            print(f'{x + y}')  # before __add__: BUG: self + self ?
            print(f'{x - y}')
            print(f'{x * y}')
            print(f'{x / y}')
            print(f'{a + b + c * d}')  # NOTE: require upg5

        else:
            print('No upg like that...')
            break


main()
