#!/usr/bin/python
from pe.toolbox import gen_primes, is_pandigital
from math import log10

def test():
    return is_pandigital(2143, end=4)

def main():
    answer = 0
    for p in gen_primes():
        end = len(str(p))
        if is_pandigital(p, end=end):
            answer = p

        if p > 100000000:
            break

    return answer


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()