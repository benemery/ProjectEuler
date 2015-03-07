import itertools
import time

from ProjectEuler.toolbox import (
    prime_factors, gen_primes, gen_primes_cached, totient_1, totient_2
)

class TestPrimes(object):
    def test_prime_factors(self):
        """Can we factorize a number correctly?"""
        #return
        assert list(prime_factors(1)) == []
        assert list(prime_factors(2)) == [(2, 1), ]
        assert list(prime_factors(4)) == [(2, 2), ]
        assert list(prime_factors(9)) == [(3, 2), ]
        assert list(prime_factors(15)) == [(3, 1), (5, 1)]

    def test_prime_gernation(self):
        """Can we generate primes correctly?"""
        primes = []
        for prime in gen_primes_cached():
            if prime > 10:
                break
            primes.append(prime)
        assert primes == [2, 3, 5, 7, ]


class TestTotient(object):
    values = [1, 2, 2, 4, 2, 6, 4, 6, 4, ]

    def test_totient_1(self):
        """Does our totient function work?"""
        for index, val in enumerate(self.values, 2):
            assert totient_1(index) == val

    def test_totient_2(self):
        """Does our totient function work?"""
        for index, val in enumerate(self.values, 2):
            assert totient_2(index) == val

    def test_totient_speed(self, pytestconfig):
        """Test speed of our totient functions"""
        N = 10000

        start = time.time()
        ans1 = totient_1(N)
        time_taken1 = time.time() - start

        start = time.time()
        ans2 = totient_2(N)
        time_taken2 = time.time() - start

        if pytestconfig.option.verbose > 0:
            print ""
            print "Totient #1: %.5fs %s" % (time_taken1, ans1)
            print "Totient #2: %.5fs %s" % (time_taken2, ans2)

        assert ans1 == ans2
        assert time_taken1 > time_taken2
