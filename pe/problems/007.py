#!/usr/bin/python
from pe.toolbox import gen_primes

def nth_prime(n):
    counter = 1
    for prime in gen_primes():
        if counter == n:
            return prime
        counter += 1

def test():
    return nth_prime(6) == 13

def main():
    return nth_prime(10001)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()