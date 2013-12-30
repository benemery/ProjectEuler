#!/usr/bin/python
from toolbox import largest_prime_divisor

def test():
    return largest_prime_divisor(13195) == 29

def main():
    return largest_prime_divisor(600851475143)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()