from toolbox import fib

def first_fib_of_length_n(n):
    for i, f in enumerate(fib()):
        if len(str(f)) == n:
            return i + 1

def test():
    return first_fib_of_length_n(3) == 12

def main():
    return first_fib_of_length_n(1000)


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()