def number_to_words(n):
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', ]

    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety', ]

    words = []

    # possibly have another list for the powers? And cycle through those?
    if n%10000 >= 1000:
        number_text = '%s thousand' % digits[int(n%10000 / 1000)]
        words.append(number_text)

    if n%1000 >= 100:
        number_text = '%s hundred' % digits[int(n%1000 / 100)]
        words.append(number_text)

    if n%100 >= 20:
        if len(words) > 0:
            words.append('and')

        number_text = tens[int(n%100 / 10)]
        if n%10 > 0:
            number_text += '-%s' % digits[n%10]
        words.append(number_text)
    elif n%100 > 0:
        #0-19
        if len(words) > 0:
            words.append('and')
        words.append(digits[n%100])

    return ' '.join(words)


def count_letters(n):
    n_in_words = number_to_words(n)
    # remove characters as defined by the question
    n_in_words = n_in_words.replace(' ', '').replace('-', '')
    return len(n_in_words)


def test():
    return count_letters(342) == 23 and count_letters(115) == 20

def main():
    count = 0
    for n in xrange(1001):
        count += count_letters(n)
    return count

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()