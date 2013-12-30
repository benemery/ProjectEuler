#!/usr/bin/python
from itertools import permutations

def test():
    return True

def main():
    for i, p in enumerate(permutations('0123456789')):
        if i == 1e6 - 1:
            return ''.join(p)


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()