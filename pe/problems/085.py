
def count_rectangles(m, n):
    """Find the number of sub rectangles in an mxn rectangle.

    Each rectangle is made up of (m + 1) * (n + 1) horizontal and vertical
    lines. Each rectangle is made up of 2 horizontal lines and 2 vertical ones.

    So, we're choosing 2 horizontal lines and 2 vertical ones, so:

        C(n + 1, 2) = (n + 1)! / 2! * (n + 1 - 2)!
                    = (n + 1)! / 2 * (n - 1)!
                    = n * (n + 1) / 2

    """
    return m * (m + 1) * n * (n + 1) / ( 2 * 2)

def test():
    return count_rectangles(3, 2) == 18

def main():
    """
    Find a rectangle with the closest number of sub rectangles to our target.
    """
    target = 2000000

    min_diff = target
    ans = None
    # These limits were found by trial and error!
    for i in xrange(1, 100):
        for j in xrange(1, 100):
            num = count_rectangles(i, j)
            diff = abs(target - num)
            if diff < min_diff:
                min_diff = diff
                ans = i * j

    return ans

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()