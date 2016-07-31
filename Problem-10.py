import math
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def is_prime(m):
	for i in xrange(2, int(math.sqrt(m)+1)):
	# for i in range(2,m):
		if (m % i) == 0:
			return 0
	else:
		return m

# print is_prime(2) # it still works

# wow this is super slowpants

def two_mills(nnnn):
	total = 0
	for i in xrange(2, nnnn):
		# print total
		total += is_prime(i)
	return total

# print two_mills(5000)
# print two_mills(10000)
# print two_mills(20000)
print two_mills(2000000)

# All this took was moving to xrange over range, and making the prime sieve go to sqrt(m)+1 instead of all the way to m... from infinite to 16.0 seconds.


