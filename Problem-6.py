# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_sq(n):
	total_sq = 0
	for e in range(1, n+1):
		total_sq += e*e
	return total_sq

print sum_sq(10)

def sq_sum(m):
	sq_total = 0
	for i in range(1, m+1):
		sq_total += i
	return sq_total*sq_total

print sq_sum(10)

print sq_sum(100) - sum_sq(100)
