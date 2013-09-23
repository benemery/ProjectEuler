def test():
    # No test
    return True

def main():
    n = 1000
    for a in range(n):
        for b in xrange(n - a):
            c = n - (a + b)
            if a+b+c==n and a*a + b*b == c*c and a<b and b<c:
                return a*b*c

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()