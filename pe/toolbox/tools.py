from math import sqrt, factorial as f
import os

def get_data(filename):
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, '..', 'problems', filename)
    with open(path, 'rb') as fin:
        data = fin.read()
    return data

def nCr(n, r):
    """ n choose r """
    return f(n) / (f(r) * f(n-r))

def fib():
    """ Returns a generator for the Fibonacci numbers """
    first, second = 0, 1
    while True:
        first, second = first + second, first
        yield first

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

def factors(n):
    """ Returns all factors of n """
    if n == 0 or n == 1:
        return set([n])

    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))

def proper_factors(n):
    """ Proper factors are factors below n """
    factors_tmp = list(factors(n))
    factors_tmp.remove(max(factors_tmp))
    return factors_tmp




def is_palindrome(n):
    """ Is a given int (or string) a palindrome? """
    n = str(n)
    return n == n[::-1]


def is_pandigital(n, start=1, end=9):
    tests = map(str, range(start, end + 1))
    n = str(n)

    if len(n) != len(tests):
        return False

    if not has_unique_digits(n):
        return False

    for digit in n:
        if digit in tests:
            tests.remove(digit)
        else:
            return False
    return len(tests) == 0


def has_unique_digits(n):
    return len(set(str(n))) == len(str(n))

def gen_triangular():
    """ Generate an infinte sequence of triangular numbers. """
    iteration = 2
    triangular = 1
    while True:
        yield triangular
        triangular, iteration = triangular + iteration, iteration+1


def cycle_length(n):
    ''' Taken straight from wikipedia,

        "A fraction in lowest terms with a prime denominator other than 2 or 5
        (i.e. coprime to 10) always produces a repeating decimal."
    '''
    # First ensure that our denominator is coprime to 10
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5

    # Now check which (if any) power of 10 reveals the cycle
    for x in range(1, n):
        if (10**x - 1) % n == 0:
            return x
    return 0

