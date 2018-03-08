# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# print 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
# print 2*3*5*7 * 2*3*2 # interesting. This is the primes, plus the extra primes needed to "make" the other numbers
# 1 is a throwaway
# 2 PRIME
# 3 PRIME
# 4 Need another 	2
# 5 PRIME
# 6 have 2 * 3
# 7 PRIME
# 8 need one more 	2
# 9 need a 			3
# 10 have 2 * 5

# print 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20

# Its the same through 10: 2*2*2*3*3*5*7
# 1	throwaway
# 2	PRIME
# 3	PRIME
# 4	need a 			2
# 5	PRIME
# 6	have 2 * 3
# 7	PRIME
# 8	need a 			2
# 9	need a 			3
# 10	have 2 * 5
# 11	PRIME
# 12	have 3 * 4
# 13	PRIME
# 14	have 2 * 7
# 15	have 3 * 5
# 16	need a 		2
# 17	PRIME
# 18	have 9 * 2
# 19	PRIME
# 20	have 4 * 5
print 2*3*5*7*11*13*17*19 * 2*2*3*2

# how do i write the code for this?

# I think the factor function can work here.
# then test if 1 - 20 are factors.
# sounds like a huge nest of if statements.
#  we only need to test: 20 (gets 10, 5, 4, 2 & 1), 19, 18 (gets 9, which gets 3), 17, 16 (gets 8), 15, 14 (gets 7), 13, 12 (gets 6) , 11
#  so test_list in range(11, 21)

def factorize(nnnnnn, mmm):
	factors = []
	for e in range(1,mmm+1):
		if nnnnnn % e == 0:
			factors.append(e)
	return factors

# print factorize(9699690, 20)
# print factorize(19399380, 20)
# print factorize(38798760, 20)
# print factorize(116396280, 20)
# print factorize(232792560, 20)

# now lets do that backwards:

# another test: for a list of n members, [1:n], factor all members and place into a new list.
def factor_complete(nn):
	complete = []
	for e in range(1, nn+1):
		complete.append(factorize(e, e))
		# print complete[e]
	return complete

gosh_darnit = factor_complete(20)
print gosh_darnit
print "that was the whole factor"

# now i have a list of lists....
def list_primes(juju):
	gots_primes = []
	temp = []
	# everything_else = []
	for e in range(len(juju)):
		if len(juju[e]) == 2:
			temp = juju[e]
			gots_primes.append(temp[1])
			# print temp
	# 	if len(juju[e]) != 2:
	# 		everything_else.append(juju[e])
	# 		# print everything_else
	# everything_else = everything_else[1:]
	return gots_primes
	# print everything_else

print list_primes(gosh_darnit)
print 'thats all the prime factors'

def others(jimmi):
	everything_else = []
	for e in range(len(jimmi)):
		if len(jimmi[e]) != 2:
			everything_else.append(jimmi[e])
	return everything_else

print others(gosh_darnit)
# that gave me two lists, one with the primes, one with everything else. now what?
# strip everything out? no -- the problem is incomplete factoring:
# 4 should be [1, 2, 2]. my factoring alg is wrong.
# 8 should be [1, 2, 2, 2]
# 9 should be [1, 3, 3]
# 16 should be [1, 2, 2, 2, 2]
# the secret i think is toal factorization, taking out those elements that match any others:

# so i need to compare two members, and iff they have the same value, remove that value. ideally, i'd start with stripping the first element (1).
# followed by stripping the last element. nope, then start the compare. so after that, im left with 

#  ok so complete rewrite. need to find all factors; so find fac1 b/t 0 to sqrt(n), then find fac2 with n/fac1
