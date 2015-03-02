from math import ceil
import fractions


def phi(n):
    """Euler's Totient function.

    Find the number of numbers below n that are relatively prime to n.
    """
    if n == 1 or n == 2:
        return 1

    result = 0
    # As gcd(k, n) == gcd(n-k, n), we only need to check half the digits
    # and add 2 to our result each time
    lim = int(ceil((n + 1.0) / 2))
    for k in xrange(1, lim):
        # Check if k is relatively prime to n
        if fractions.gcd(n, k) == 1:
            result += 2
    return result

def find_largest_ratio(limit):
    winner = 0
    winning_ratio = 0
    for n in xrange(2, limit+1):
        phi_n = phi(n)
        ratio = 1.0 * n / phi_n
        print n, phi_n, ratio

        if ratio > winning_ratio:
            winner = n
            winning_ratio = ratio
    return winner

def test():
    return find_largest_ratio(10) == 6

def main():
    return find_largest_ratio(100)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()


