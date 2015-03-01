from math import sqrt, factorial as f
import os

def get_data(filename):
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, filename)
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


# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    """ Generate an infinite sequence of prime numbers. """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def get_primes(n):
    """ Helper function to get all the primes below n.
        Fine if you're dealing with a low n, otherwise you may want to watch mem
        usage.
    """
    primes = []
    for p in gen_primes():
        if p > n:
            break
        primes.append(p)
    return primes

def is_prime(n):
    """ Test for primility.
        Limit is set as such as the sqrt(n) is the largest divisor pair
        (larger divisors will have partner below sqrt(n)).
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    lim = int(sqrt(n))+1
    for i in xrange(3, lim, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True

def is_cyclic_prime(n):
    n = str(n)
    # check if any digit is even, if so don't bother with anything else
    for d in n:
        if int(d) % 2 == 0:
            return n == '2'

    cycles = [[n[i - j] for i in range(len(n))] for j in range(len(n))]
    # join the digits and convert to ints
    cycles = map(lambda x: int(''.join(x)), cycles)
    for p in cycles:
        if not is_prime(p):
            return False
    return True


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