#!/usr/bin/python
from pe.toolbox import is_palindrome

def is_palindromic_in_2_bases(n):
    """ is n a palindrome in base 10 and base 2? """
    return is_palindrome(n) and is_palindrome("{0:b}".format(n))

def test():
    return is_palindromic_in_2_bases(585)

def main():
    return sum(filter(is_palindromic_in_2_bases, xrange(1000000)))


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()
