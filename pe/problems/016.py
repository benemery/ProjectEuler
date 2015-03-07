#!/usr/bin/python
def sum_digits(n, power):
    return sum(map(int, list(str(pow(n, power)))))

def test():
    return sum_digits(2, 15) == 26

def main():
    return sum_digits(2, 1000)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()