def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a > b:
        return gcd(b,a)
    elif b % a == 0:
        return a
    else:
        return gcd(a, b % a)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    def hailstone_count(n, count):
        print(n)
        if n == 1:
            return count
        elif n % 2 == 0:
            return hailstone_count(n // 2, count + 1)
        else:
            return hailstone_count(n * 3 + 1, count + 1)
    return hailstone_count(n, 1)
