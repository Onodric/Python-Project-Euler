import math
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# this is shit, and I need to clean it up and make sense of it. I understand fermat's method and reasoning a bit better now...

#  so we need to:
	# 1. input a number
def is_prime(m):
	for i in range(2,m): # this should go to int(sqrt(m))+1 because reasons: factors come in pairs, the largest of which can only ever be sqrt(m).
		if (m % i) == 0:
			return ""
	else:
		return m

def large_prime(n):
	factors = []
	# primes = []
# 	2. find its factors
	if n > 1:
		for entire_number in range(2, int(math.sqrt(n)) + 1):
			# print entire_number
			if (n % entire_number) == 0: # so this is a factor. Lets test it.
				if is_prime(entire_number) == "":
					"""break"""
				else:
					factors.append(is_prime(entire_number))
				# for prime_check in range(2, entire_number + 1):
					# print "    ", prime_check
					# if (entire_number % prime_check) == 0:
					# 	break
					# entire_number not in factors:
							# factors.append(entire_number)
		return factors[-1]
# 	3. find the prime ones
# def find_prime(n):
# 	primes = []
# 	for factor_number in range(2, n): # hmm... is it prime?
# 		if n % factor_number == 0:
# 			print 'not prime'
# 		else:
# 			primes.append(factor_number)
	#		factors.append(entire_number)
	#		print factors
# 	4. output the bigest one
	# return factors[-1]
	# return primes
#

# print large_prime(20)
print large_prime(600851475143)
# print find_prime(100)
print is_prime(2345345)

# for num in range(lower,upper + 1):
#    # prime numbers are greater than 1
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)