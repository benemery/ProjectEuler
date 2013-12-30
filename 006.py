#!/usr/bin/python
def sum_square_difference_for_range(x, y):
    nums = range(x, y + 1)
    return sum(nums) * sum(nums) - sum(map(lambda x: x*x, nums))

def test():
    return sum_square_difference_for_range(1, 10) == 2640

def main():
    return sum_square_difference_for_range(1, 100)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()