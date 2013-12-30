#!/usr/bin/python
from toolbox import is_cyclic_prime

def number_of_cyclic_primes_below_n(n):
    if n < 2:
        return 0
    # let's ensure n is odd so we only bother testing odd numbers, and that
    # we have a sufficiently high value to pass to range so that we include the
    # upper value
    if n % 2 == 0:
        n += 1
    else:
        n += 2

    answer = 1
    for p in xrange(3, n, 2):
        if is_cyclic_prime(p):
            answer += 1
    return answer

def test():
    return number_of_cyclic_primes_below_n(100) == 13

def main():
    return number_of_cyclic_primes_below_n(1000000)


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()
