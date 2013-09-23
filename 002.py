from toolbox import fib
from itertools import takewhile

def test():
    # No test given
    return True

def main():
    fibs = takewhile(lambda x: x<4e6, fib())
    even_fibs = [n for n in fibs if n%2==0]
    return sum(even_fibs)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()