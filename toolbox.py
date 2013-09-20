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

def prime_factors(n):
    """ Returns all the prime factors of a positive integer """
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:  # test for divisor
            factors.append(d)
            n /= d  # by reducing our target, we are removing multiples of d (ensuring d is prime)
        d = d + 1

    return factors


def is_palindrome(n):
    """ Is a given int (or string) a palindrome? """
    n = str(n)
    return n == n[::-1]