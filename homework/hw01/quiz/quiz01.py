def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    minNum = min(a,b)
    while minNum > 0:
        if a % minNum == 0 and b % minNum == 0:
            return a * b // minNum
        else :
            minNum -= 1

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    my_set = set()
    count = 0
    while True:
        num = n % 10
        n = n // 10
        my_set.add(num)
        if n == 0:
            break
    return len(my_set)

