import fractions
from math import ceil
from operator import mul

from . import prime_factors

def totient_1(n):
    """Euler's Totient function.

    This is a simple approach that tests for a common divisor for all
    k below our limit.
    """
    if n == 1 or n == 2:
        return 1

    result = 0
    # As gcd(k, n) == gcd(n-k, n), we only need to check half the digits
    # and add 2 to our result each time
    lim = int(ceil((n + 1.0) / 2))
    for k in xrange(1, lim):
        # Check if k is relatively prime to n
        if fractions.gcd(n, k) == 1:
            result += 2
    return result


def totient_2(n):
    """Euler's Totient function.

    Here we make use of a known fact about primes, if n is prime, then
    all k for 0 < k < n is relatively prime to n. Thus we have p - 1 as
    our totient.

    Furthermore, this function is multiplicative, i.e.

    phi(n * m) = phi(n) * phi(m)

    So, if we can write n as:

    n = p_1 * p_2 * p_3 ... * p_n

    Where p is prime, then we know the totient to be

    phi(n)  = phi(p_1 * p_2 * p_3 * .. p_n)
            = phi(p_1 - 1) * phi(p_2 - 1) * phi(p_3 - 1) * ... *  phi(p_n - 1)
    """
    factors = prime_factors(n)
    totients = ((p - 1) * p ** (exponent - 1) for p, exponent in factors)
    return reduce(mul, totients, 1)

# Add the primary totient function to our namespace (makes imports cleaner)
totient = totient_2
