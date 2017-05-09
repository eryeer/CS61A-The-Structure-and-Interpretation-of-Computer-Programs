HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n == 1 or n == 2 or n == 3:
        return n
    else:
        term1, term2, term3 = 2, 1, 0
        result = 3
        i = 4
        while i <= n:
            term1, term2, term3 = result, term1, term2 
            result = term1 + 2 * term2 + 3 * term3
            i += 1
        return result

        

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    return get_pingpong(n)

def get_pingpong(n):
    seq = [1]
    i = 1
    flag = 1
    if n == 1:
        return seq[0]
    while i < n:
        if flag == 1:
            seq = seq + [seq[i - 1] + 1]
        else:
            seq = seq + [seq[i - 1] - 1]
        if (i + 1) % 7 == 0 or contain_seven(i + 1):
            flag = switch_dir(flag)
        i += 1
    return seq[n - 1]

def switch_dir(x):
    """return 0 or 1"""
    return 1 - x

def contain_seven(n):
    while n != 0:
        left, remainder = n // 10, n % 10
        if remainder == 7:
            return True
        n = left
    return False

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    m = great_two_power(amount)
    return count_partition(amount, m)


def great_two_power(n):
    i = 0
    while True:
        if 2 ** i <= n and 2 ** (i + 1) > n:
            return 2 ** i
        i += 1

def count_partition(n,m):
    if m == 0:
        return 0
    elif n < 0:
        return 0
    elif n == 0:
        return 1        
    else:
        with_m = count_partition(n-m,m)
        without_m = count_partition(n,m//2)
        return with_m + without_m

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda x: 1 if x == 1 else mul(x, )
