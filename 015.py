from toolbox import gen_triangular, factors

def triangular_with_more_than_n_divisors(n):
    for t in gen_triangular():
        if len(factors(t)) > n:
            return t

def test():
    return triangular_with_more_than_n_divisors(5) == 28

def main():
    return triangular_with_more_than_n_divisors(500)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()