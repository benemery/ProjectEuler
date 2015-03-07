#!/usr/bin/python
from pe.toolbox import factors

def test():
    return True

def main():
    # find all the abundant numbers below the limit 28123 (given in question)
    abundant = []
    upper_limit = 28123

    # NOTE: we know that any abundant number n, any multiple of n will also be
    # abundant. How can we use this? (At the moment we don't.)

    for n in xrange(upper_limit + 1):
        # Finding the factors is fast, but the sum includes n. So subtract n.
        if sum(factors(n)) - n > n:
            abundant.append(n)

    # We want to find all the numbers that cannot be reached by summing two
    # abundant numbers

    # List the numbers that we're unsure if they can be reached
    nums = range(upper_limit)
    # Perform each addition and set the corresponding index to 0. Then return
    # the sum of the remainging digits.
    for start_index, a in enumerate(abundant):
        for b in abundant[start_index:]:
            if a + b >= upper_limit:
                # no need to continue
                break
            nums[a + b] = 0

    return sum(nums)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()