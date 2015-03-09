#!/usr/bin/python
from pe.toolbox import prime_factors
from collections import defaultdict, Counter

def lowset_common_multiple_for_range(x, y):
    """
        This is the first problem that requires some thought! We know from the nature
        of the problem that this has something to do with divisors, but what?

        By finding all the prime divisors within our range, we know what the answer
        must be divisible by. By then finding the largest power for each prime factor,
        we find the largest common prime factor (^power) shared between the answer and something
        in our range.

        So then, by multiplying all the largest occurences of our prime factors,
        we reach the correct answer!
    """
    highest_prime_divisors = defaultdict(int)  # hold the highest power for a prime divisor (so for 2,4,8, this would hold 2^3)

    for n in range(x, y + 1):
        for prime, expo in prime_factors(n):
            factor = pow(prime, expo)
            if highest_prime_divisors[prime] < factor:
                highest_prime_divisors[prime] = factor

    return reduce(lambda a, b: a*b, highest_prime_divisors.values())

def test():
    return lowset_common_multiple_for_range(1, 10) == 2520

def main():
    return lowset_common_multiple_for_range(1, 20)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()