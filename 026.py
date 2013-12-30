#!/usr/bin/python
from toolbox import is_prime

def longest_cycle(n):
    ''' We only need to test primes as any other composite will have the same
        cycle length.

        We're searching for a Full Reptend Prime
        http://mathworld.wolfram.com/FullReptendPrime.html

        So we want to find the largest FRP below n (so we can start at n and
        work backwards).
    '''
    # We can speed this up by only looking at odd numbers
    if n % 2 == 0:
        n -= 1

    for p in range(n, 1, -2):
        if not is_prime(p):
            # not prime, ignore
            continue

        # now, increase powers of 10 and see if we have a FRP
        # Note: we need to find the minimum value of k that this holds for, we
        #   can't simply check pow(10, p-1)
        k = 1
        while pow(10, k) % p != 1:
            k += 1

        if p-k == 1:
            # Found a FRP!
            break
    return p



def test():
    return longest_cycle(10) == 7

def main():
    return longest_cycle(1000)


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()