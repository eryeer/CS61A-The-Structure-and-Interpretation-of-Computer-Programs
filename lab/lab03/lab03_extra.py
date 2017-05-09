from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: (x % 10) + 10 * y
    while x > 0:
        x, y = x // 10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n== 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        print(i)
        if i == n:
            return
        else:
            counter(i+1)
    counter(1)

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if a == 0 or b == 0:
        return c 
    elif b == 1:
        return a + c
    else:
        return a + ab_plus_c(a, b-1, c)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def check_prime(i):
        if i == n:
            return True
        elif n % i == 0:
            return False 
        else:    
            return check_prime(i+1)
    return check_prime(2)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    def odd_sum(i):
        if i == n:
            return odd_term(i)
        else:
            return odd_term(i) + even_sum(i+1)
    def even_sum(i):
        if i == n:
            return even_term(i)
        else:
            return even_term(i) + odd_sum(i+1)
    return odd_sum(1)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def helper(i, j, count):
        if j == 0:
            return count + ten_pairs(n // 10)
        else:
            if i + j % 10 == 10:
                return helper(i, j // 10, count + 1)
            return helper(i, j//10, count)
    if n < 10:
        return 0
    return helper(n % 10, n // 10, 0)
