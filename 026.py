from toolbox import is_prime

def cycle_length(n):
    ''' Taken straight from wikipedia,

        "A fraction in lowest terms with a prime denominator other than 2 or 5
        (i.e. coprime to 10) always produces a repeating decimal."
    '''
    # First ensure that our denominator is coprime to 10
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5

    # Now check which (if any) power of 10 reveals the cycle
    for x in range(1, n):
        if (10**x - 1) % n == 0:
            return x
    return 0

def longest_cycle(n):
    ''' Quite brute forcey..
        Find all the cycle lengths, take the biggest.

        I think this can be improved..
        http://en.wikipedia.org/wiki/Repeating_decimal#Fractions_with_prime_denominators
    '''
    answer = 0
    test = 0
    for i in range(1, n):
        if cycle_length(i) > test:
            test = cycle_length(i)
            answer = i

    return answer

def test():
    return longest_cycle(10) == 7

def main():
    return longest_cycle(1000)


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()