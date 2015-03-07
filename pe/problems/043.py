#!/usr/bin/python
from itertools import permutations

from pe.toolbox import is_pandigital

def test_for_crazy_properties(num):
    ''' Integer representation of a given string '''
    if not is_pandigital(num, start=0):
        return False

    digits = [digit for digit in str(num)]

    # set up the digit + divisor pairs
    pairs = [((2, 3, 4), 2), ((3, 4, 5), 3), ((4, 5, 6), 5), ((5, 6, 7), 7),
                ((6, 7, 8), 11), ((7, 8, 9), 13), ((8, 9, 10), 17)]

    # test each pair, break if we fail a test
    for test_digits, divisor in pairs:
        num = int(''.join([digits[test_digit - 1]
                            for test_digit in test_digits]))

        # Test the divisor
        if num % divisor != 0:
            return False

    return True

def test():
    return test_for_crazy_properties(1406357289)

def main():
    result = 0
    for perm in permutations(range(10)):
        num = int(''.join([str(digit) for digit in perm]))
        if test_for_crazy_properties(num):
            result += num

    return result

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()