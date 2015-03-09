"""Any prime number based funcionality lives in here."""

from math import sqrt

def prime_factors(n):
    """Find all the prime factors of a `n`.

    We return a generator of prime + exponent pairs for each prime
    factor.
    """
    for prime in gen_primes_cached():
        if prime > n:
            return

        exponent = 0
        while n % prime == 0:  # test for divisor
            n /= prime
            exponent += 1
        if exponent != 0:
            yield prime, exponent

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

composites = {}
primes = []
def gen_primes_cached():
    # Running integer to be tested
    prime = 2

    # First yeild all known primes, then find new ones
    for prime in primes:
        yield prime

    while True:
        if prime not in composites:
            primes.append(prime)
            composites[prime * prime] = [prime]

            yield prime
        else:
            for p in composites[prime]:
                composites.setdefault(prime + p, []).append(p)
            del composites[prime]
        prime += 1

from itertools import islice, cycle, count, compress

def croft():
    """Yield prime integers using the Croft Spiral sieve.
 
    This is a variant of wheel factorisation modulo 30.
    """
    # Copied from:
    #   https://code.google.com/p/pyprimes/source/browse/src/pyprimes.py
    # Implementation is based on erat3 from here:
    #   http://stackoverflow.com/q/2211990
    # and this website:
    #   http://www.primesdemystified.com/
    # Memory usage increases roughly linearly with the number of primes seen.
    # dict ``roots`` stores an entry x:p for every prime p.
    for p in (2, 3, 5):
        yield p
    roots = {9: 3, 25: 5}  # Map d**2 -> d.
    primeroots = frozenset((1, 7, 11, 13, 17, 19, 23, 29))
    selectors = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
    for q in compress(
            # Iterate over prime candidates 7, 9, 11, 13, ...
            islice(count(7), 0, None, 2),
            # Mask out those that can't possibly be prime.
            cycle(selectors)
            ):
        # Using dict membership testing instead of pop gives a
        # 5-10% speedup over the first three million primes.
        if q in roots:
            p = roots[q]
            del roots[q]
            x = q + 2*p
            while x in roots or (x % 30) not in primeroots:
                x += 2*p
            roots[x] = p
        else:
            roots[q*q] = q
            yield q


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
