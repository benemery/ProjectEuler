#!/usr/bin/python
def test():
    # Test is pretty poor
    return True

def main():
    names = open('022_names.txt', 'r').read()
    # turn to a list of names
    names = names.replace('"', '').split(',')
    names.sort()

    answer = 0
    for index, name in enumerate(names):
        # NOTE: the answer is indexed from one whereas enumerate is indexed at 0
        answer += (index + 1) * sum([ord(letter) - 64 for letter in list(name)])
    return answer

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()