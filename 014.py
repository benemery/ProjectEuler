def gen_collatz(n):
    while n > 1:
        yield n
        if n%2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
    yield n


def test():
    return len(list(gen_collatz(13))) == 10

def main():
    # this runs in 40s, surely it can be approved?
    # maybe map previously seen numbers to their distance from 1?
    max = 0
    answer = 0
    for i in xrange(50001, 1000000):  # we only need to go from 500,000 as that's the first step after 1000000
        temp = len(list(gen_collatz(i)))
        if temp > max:
            max = temp
            answer = i
    return answer

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()