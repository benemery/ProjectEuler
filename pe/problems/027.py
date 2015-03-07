#!/usr/bin/python
from pe.toolbox import is_prime, get_primes

def number_of_consecutive_primes(a, b):
    n = 0
    while is_prime(n*n + a*n + b):
        n += 1
    return n

def test():
    return number_of_consecutive_primes(a=1, b=41) == 40 and \
                number_of_consecutive_primes(a=-79, b=1601) == 80

def main():
    ''' Checks every value of a, but only primes of b as we notice that for n=0
        b must be prime.
    '''
    answer = 0
    test = 0

    b_primes = get_primes(1000)

    for a in xrange(-1000, 1000):
        for b in b_primes:
            num = number_of_consecutive_primes(a, b)
            if num > test:
                test = num
                answer = a * b
    return answer

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()