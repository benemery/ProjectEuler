from math import factorial as f

def sum_factorial_digits(n):
    return sum(f(int(i)) for i in str(n))

def test():
    return sum_factorial_digits(145) == 145

def main():
    # Seek to find the number of non-repeating chains below one million
    # that have 60 terms

    # Upper limit
    lim = 1000000

    # First populate a cache of the factorials so we don't repeat them
    factorials = dict((str(n), f(n)) for n in range(10))

    # Cache chain lengths
    chain_lengths = {}

    for n in xrange(lim):
        current_chain = []
        current_chain.append(n)

        new = n
        while True:
            new = sum(factorials[i] for i in str(new))

            if new in chain_lengths:
                # We know how long this chain is
                break

            if new in current_chain:
                # repeated digit, chain is over
                break
            current_chain.append(new)

        # Find the additional contribution from the last sum
        additional_size = chain_lengths.get(new, 0)

        for i, num in enumerate(current_chain):
            if num not in chain_lengths:
                chain_lengths[num] = additional_size + len(current_chain) - i

    # Find all chains that are 60 sections long before they repeat
    # Note: in python, True is treated as 1 and False as 0
    solution = sum(value == 60 for value in chain_lengths.values())

    return solution

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()
