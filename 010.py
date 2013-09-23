from toolbox import gen_primes

def sum_primes_below(n):
    total = 0
    for prime in gen_primes():
        if prime < n:
            total += prime
        else:
            break
    return total

def test():
    return sum_primes_below(10) == 17

def main():
    return sum_primes_below(2000000)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()