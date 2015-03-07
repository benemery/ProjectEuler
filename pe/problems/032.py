#!/usr/bin/python
from pe.toolbox import is_pandigital, has_unique_digits

def test():
    return True

def main():
    """
        We're looking for numbers which x * y = z and the concatination of
        x, y and z are 1-9 pandigital.

        We can approach this problem from z. We know we need nine digits, the
        only way to get 9 is to have a 1-digit * 4-digit = 4-digit or to have
        a 2-digit * 3-digit = 4-digit.
    """
    results = set()
    for z in range(1234, 9876):
        if not has_unique_digits(z):
            # repeated digits, continue
            continue

        # check values of x to see if they can divide z
        for x in range(2, 99):
            if z % x == 0:
                y = z / x
                if is_pandigital('%s%s%s' % (x, y, z)):
                    results.add(z)

    return sum(results)


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()