from math import ceil
import fractions

from pe.toolbox import totient, totient_1, gen_primes


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

def find_largest_ratio_3(limit):
    winner = 0
    winning_ratio = 0

    skipable = set()
    previous = {}
    for n in xrange(2, limit + 1):
        if n in skipable:
            skipable.remove(n)
            skipable.add(2 * n)
            continue

        if n in previous:
            phi_n = previous[n]
            del previous[n]
        else:
            phi_n = totient(n)

        ratio = 1.0 * n / phi_n
        if ratio > winning_ratio:
            winner = n
            winning_ratio = ratio
            print n, winning_ratio

        if not n % 2:
            skipable.add(2 * n)
        else:
            previous[2 * n] = phi_n
    return winner


def find_largest_ratio_4(limit):
    """We're looking to find the largest value for n / phi(n).

    This means that we want to minimise phi(n). Let's look at some
    properties of phi(n).

    Phi is mulitiplicitive and n can written in terms of prime divisors,
    ie.

    phi(n)  = phi(p_1 * p_2 * ... * p_n)
            = phi(p_1) * phi(p_2) * .. * phi(p_n)

    and

    phi(p^k) = p^(k-1) * (p - 1)

    then

    phi(n)  = (p_1 - 1) * (p_2 - 1) * .. * (p_n - 1), for k = 1.

    where p is prime.

    Using this we can see that the lower bound for phi(n) is found for
    numbers that have single power, small prime factors,
    """
    ans = 1
    ans_new = ans
    for prime in gen_primes():
        ans_new *= prime
        if ans_new > limit:
            return ans
        ans = ans_new


def test():
    return find_largest_ratio_4(10) == 6

def main():
    N = 1000000
    x = find_largest_ratio_4(N)
    return x

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()


