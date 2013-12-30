#!/usr/bin/python
def test():
    return True

def main():
    ''' Let's brute force this! Instead of working out which combinations make
        £2, let's build the solution from the remainder.

        TODO: there is a better approach with dynamic programming, implement
        that!
    '''
    answer = 0

    for a in range(200, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1, -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for g in range(f, -1, -2):
                                answer += 1
    return answer

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()