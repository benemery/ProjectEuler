from itertools import takewhile

def fib():
    """ Returns a generator for the Fibonacci numbers """
    first, second = 0, 1
    while True:
        yield first
        first, second = first + second, first

def largest_prime_divisor(n):
    """ Find the largest prime divisor of a number """
    i = 1
    while i * i < n:  # sqrt of n is the upper limit
        if n%i == 0:  # we have a divisor, lower n to the larger divisor
            n = n / i
        i += 1
    # we have continually set n to the largest of two divisors, what remains
    # is the largest divisor, which has no other divisors, and is therefore prime!
    return n

def is_palindrome(n):
    """ Is a given int (or string) a palindrome? """
    n = str(n)
    return n == n[::-1]