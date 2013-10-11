def sum_of_digits_to_power(n):
    ''' Find (and sum) the numbers which can be written as the sum of their
        digits to power n.
    '''
    nums = []
    # the max that we can reach is 9^n * the number of digits
    i = 1
    while pow(9, n) * i > pow(10, i):
            i += 1
    lim = pow(9, n) * i

    # keep a map of all the powers so we're not repeating expensive operations
    pows = {}
    for d in '0123456789':
        pows[d] = pow(int(d), n)

    # go!
    for a in range(2, lim):
        total = 0
        for digit in str(a):
            total += pows[digit]
            if total > a:
                break
        if total == a:
            nums.append(a)

    return sum(nums)

def test():
    return sum_of_digits_to_power(4) == 19316

def main():
    return sum_of_digits_to_power(5)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()