from toolbox import is_palindrome

def largest_palindrome(num_digits):
    ans = -1
    i_lower = pow(10, num_digits - 1)
    i_upper = pow(10, num_digits) - 1

    upper_limit = i_upper * i_upper

    for n in xrange(upper_limit, 0, -1):
        # start at the upper limit, going back
        if is_palindrome(n):
            # find the lowest divisor
            for i in xrange(i_lower, i_upper):
                if n % i == 0 and n / i >= i_lower and n / i <= i_upper:
                    ans = n
                    break

                if i * i > n:
                    break

        if ans > -1:
            # answer has been found
            break

    return ans

def test():
    return largest_palindrome(num_digits=2) == 9009

def main():
    return largest_palindrome(num_digits=3)

if __name__ == '__main__':
    print "Passes test?", test()
    print "Answer:", main()
