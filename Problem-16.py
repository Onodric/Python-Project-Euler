# 2^15 = 32768; the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

# import math

# print (2**1000)

def find_sum(base, power): # a function to find the sum of the digits of an exponetial power
	raw_number = 0
	raw_str = ''
	total_of_digits = 0
	raw_number = base**power
	raw_str = str(raw_number)
	for i in range(len(raw_str)):
		total_of_digits += int(raw_str[i])
	return total_of_digits

print find_sum(2,15)
print find_sum(2, 1000)
