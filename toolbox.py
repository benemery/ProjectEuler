def fib():
	'''
		Returns a generator for the Fibonacci numbers
	'''
	first, second = 0, 1
	while True:
		yield first
		first, second = first + second, first
