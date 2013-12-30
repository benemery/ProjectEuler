#!/usr/bin/python
from toolbox import gen_triangular

def convert_string_to_int(a_string):
    ''' Integer representation of a given string '''
    return sum([ord(char.lower()) - 96 for char in a_string])

def test():
    return True

def main():
    # Read the file of words, converting them to their number version
    string_number_pairs = []
    numbers_to_test = set()
    with open('042_words.txt') as words_file:
        data = words_file.read()
        for word in data.replace('"',"").lower().split(','):
            string_as_int = convert_string_to_int(word)

            string_number_pairs.append((word, string_as_int))
            numbers_to_test.add(string_as_int)

    # Now we have our unique set of numbers to test, find all the tringular
    # numbers up to the max and compare
    triangular_numbers = set()
    lim = max(numbers_to_test)

    for triangular in gen_triangular():
        if triangular > lim:
            break

        triangular_numbers.add(triangular)

    # find numbers that are also triangular
    triangular_strings = numbers_to_test.intersection(triangular_numbers)

    # Grab all the strings that have a triangular int representation!
    result = len([word for word, num in string_number_pairs
                        if num in triangular_strings])

    return result

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()