#!/usr/bin/python
from toolbox import nCr

def lattice_paths(x, y):
    # we need to take x+y steps to reach one corner of the lattice to the other.
    # if we took x+y steps horizontally we'd be pretty off target.
    # thus we need to choose y steps to flip to being vertical.
    return nCr(x+y,y)

def test():
    return lattice_paths(2, 2) == 6

def main():
    return lattice_paths(20, 20

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()