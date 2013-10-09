def distinct_terms(lim_a, lim_b):
    # By using a set we already only keep distinct terms
    terms = set()
    for a in range(2, lim_a+1):
        for b in range(2, lim_b+1):
            terms.add(pow(a, b))

    return len(terms)

def test():
    return distinct_terms(5, 5) == 15

def main():
    return distinct_terms(100, 100)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()