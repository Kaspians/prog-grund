# skapa classen Frac (already exist similar called `Fraction`)

# ===========================================================================
# upg1
# ===========================================================================


def gcd(a: int, b: int) -> int:
    while True:
        t = b
        b = a % b
        a = t
        if b == 0:
            break
    return a


print('a', gcd(int(input('a')), int(input('b'))))
