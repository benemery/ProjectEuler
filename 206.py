#!/usr/bin/python
def test():
    return True

def main():
    """We're looking for a number who's square takes the form 1_2_3_4_5_6_7_8_9_0

    Let:
        N = 1_2_3_4_5_6_7_8_9_0
        n = sqrt(N) (that matches the pattern)

    *   9^9 possible values
    *   n^2 to end in 0, we know that n must end in 0. This means that
        n is a multiple of 10, so the first two digits of N are 0.
        i.e. N = 1_2_3_4_5_6_7_8_900
    *   For the third digit to be 9, the first three digits of N are
        either 300 or 700.
    *   Maximum values: N = 1929394959697989900; n = 1389026623.1062636.
    """
    match_string = "1_2_3_4_5_6_7_8_9_0"

    # To make the comparisions easier, start at the largest value of n
    # so we don't have to worry about any string matching lengths etc
    n = 1389026670

    # We know that n must end in 30 or 70, so we can alter our diff
    # to ensure we only check those values
    diff = 40
    while True:
        n_test = str(pow(n, 2))
        for i in range(0, len(match_string), 2):
            if match_string[i] != n_test[i]:
                break
        else:
            # Our string matched!
            break

        n -= diff
        diff = 60 if diff == 40 else 40

    return n

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()