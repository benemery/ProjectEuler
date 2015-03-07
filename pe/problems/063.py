#!/usr/bin/python
from pe.toolbox import fib

def does_power_match_length(i, n):
    """Does the interger i, when raised to the power n have n digits?"""
    num = pow(i, n)
    return len(str(num)) == n

def test():
    return does_power_match_length(7, 5) and does_power_match_length(8, 9)

def main():
    """
        *   10^n for positive interger n will always have n+1 digits - so
            10 is our limit.
        *   if i^n != n digits, then i^(n+1) will not have n+1 digits.
    """
    answer = 0

    for i in range(1, 10, 1):
        n = 1
        while True:
            if does_power_match_length(i, n):
                answer += 1
                n += 1
            else:
                break

    return answer

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()