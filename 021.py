#!/usr/bin/python
from toolbox import proper_factors, factors

def d(n):
    return sum(proper_factors(n))

def test():
    a = 220
    b = d(a)
    return b == 284 and d(b) == a

def main():
    seen = set()
    for a in range(10001):
        b = d(a)
        if a not in seen and d(b) == a and b != a:
            seen |= set([a, b])
    return sum(seen)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()