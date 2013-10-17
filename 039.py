from math import sqrt

def number_of_integer_right_triangles(p):
    answer = 0
    for a in range(1, p-1):
        for b in range(a, p-a-1):
            c2 = a*a + b*b
            c = sqrt(c2)

            if a + b + c != p:
                continue

            # whole number?
            if c % 1 == 0:
                answer += 1

    return answer

def test():
    return number_of_integer_right_triangles(120) == 3

def main():
    answer = 0
    test = 0
    for p in range(1, 1001):
        temp = number_of_integer_right_triangles(p)
        if temp > test:
            test = temp
            answer = p
    return answer


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()
