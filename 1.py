def sum_multiples(n):
	return sum([i for i in range(n) if i%3 == 0 or i%5 == 0])

def test():
	return sum_multiples(10) == 23

def main():
	return sum_multiples(1000)

if __name__ == '__main__':
	print "Passes test? ", test()
	print "Answer: ", main()