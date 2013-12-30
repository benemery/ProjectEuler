#!/usr/bin/python
from fractions import Fraction

def cancels_unusually(n , d):
    if n % 10 == 0 or d % 10 == 0:
        return False

    n_digits = set(str(n))
    d_digits = set(str(d))
    duplicate = n_digits.intersection(d_digits)
    if len(duplicate) == 1 and len(n_digits) == 2 and len(d_digits) == 2:
        # Common factor in both
        n_cancel = float((n_digits - duplicate).pop())
        d_cancel = float((d_digits - duplicate).pop())
        return d_cancel != 0 and n_cancel / d_cancel == float(n) / d
    return False

def test():
    return cancels_unusually(49, 98)

def main():
    fractions = []
    for n in range(11, 100):
        for d in range(n + 1, 100):
            if cancels_unusually(n, d):
                fractions.append((n, d))

    # multiply through
    f = reduce(lambda a, b: (a[0] * b[0], a[1] * b[1]), fractions)
    # use Fraction to reduce f for us
    final = Fraction(f[0], f[1])

    return final.denominator

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()
