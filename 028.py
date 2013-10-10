def sum_spirals(n):
    """ We're summing the corners of a n * n spiral where n is odd
    """
    answer = 0
    position = 1
    increment = 2
    end = n*n
    while True:
        for i in range(4):
            # add each corner
            answer = answer + position
            position += increment
            # Have we passed the final corner?
            if position > end:
                return answer
        # the next shell increase the row length by 2
        increment += 2

def test():
    return sum_spirals(5) == 101

def main():
    return sum_spirals(1001)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()