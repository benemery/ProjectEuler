#!/usr/bin/python
from math import factorial as f

# Let's cache all the factorials we know we'll be using
factorials = {}
for d in '0123456789':
    factorials[d] = f(int(d))

def is_factorian(n):
    ''' Does the sum factorial of the digits of n equal n? '''
    digits = str(n)
    if len(digits) <= 1:
        return False
    return sum([factorials[i] for i in digits]) == n

def test():
    return is_factorian(145)

def main():
    # the max that we can reach is 9! * the number of digits
    i = 1
    lim = f(9)
    while lim * i > pow(10, i):
        i += 1
    lim *= i

    return sum([n for n in xrange(lim + 1) if is_factorian(n)])


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()
