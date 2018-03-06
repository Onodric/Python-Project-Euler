# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def is_prime(k):
	for i in range(2,k):
		if (k % i) == 0:
			return 0
	else:
		return 1

def find_prime(m):
	counter = 0 # this is the number of the prime
	num = 1 # we are testing this one start at two
	n = 2
	while counter < m: # test case will be 7
		num += 1 # increase the test number every loop
		counter += is_prime(num)
		# for n in range(1, int(math.sqrt(num)) + 1):
		# 	if == 0:
		# 		counter += 0
		# 	else:
		# 		counter += 1				
		print "counter = ", counter, " ; ", "num = ", num, " ; ", "n = ", n
	return num


	# while num < 1000:
	# 	while counter <= n:
	# 		counter += is_prime(num)
	# 	num += 1
	# 	print counter, num
	# return num

print is_prime(18)

# print find_prime(6)
print find_prime(10)
print find_prime(15)
print find_prime(10001)
