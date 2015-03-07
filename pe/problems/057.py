#!/usr/bin/python

def root_two_continual_fraction():
    p, q = 1, 0
    while True:
        yield p, q
        p, q = p + 2 * q, p + q

def test():
    for p, q in root_two_continual_fraction():
        if len(str(p)) > len(str(q)):
            break

    return p == 1393 and q == 985

def main():
    answer = 0
    index = 0
    for p, q in root_two_continual_fraction():
        if len(str(p)) > len(str(q)):
            answer += 1

        index += 1
        if index >= 1000:
            break

    return answer


if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()
