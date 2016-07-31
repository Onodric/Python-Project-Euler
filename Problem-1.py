# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def problem_1(num, mult_1, mult_2):
	sum = 0
	for e in range(num):
		if e % mult_1 == 0 or e % mult_2 == 0:
			sum += e
	return sum

print problem_1(10, 3, 5)
print problem_1(1000, 3, 5)

# this works.
