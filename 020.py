#!/usr/bin/python
from math import factorial as f

def sum_factorial(n):
    return sum(map(int, list(str(f(n)))))

def test():
    return sum_factorial(10) == 27

def main():
    return sum_factorial(100)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()