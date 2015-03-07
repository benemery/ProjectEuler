from math import ceil
import fractions

from pe.toolbox import totient, totient_1


def find_largest_ratio(limit):
    winner = 0
    winning_ratio = 0
    for n in xrange(2, limit+1):
        phi_n = totient_1(n)
        ratio = 1.0 * n / phi_n

        if ratio > winning_ratio:
            winner = n
            winning_ratio = ratio

    print '###', winner, winning_ratio
    return winner

def find_largest_ratio_2(limit):
    winner = 0
    winning_ratio = 0
    for n in xrange(2, limit+1):
        phi_n = totient(n)
        ratio = 1.0 * n / phi_n

        # print n, phi_n

        if ratio > winning_ratio:
            winner = n
            winning_ratio = ratio

    print '###', winner, winning_ratio
    return winner

def test():
    return find_largest_ratio(10) == 6

def main():
    import time
    start = time.time()
    x = find_largest_ratio_2(10000)
    print time.time() - start
    return x

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()


