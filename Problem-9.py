# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def possibles(nnnn): # where nnnn is the target sum
	a = 1
	b = 1
	c = 1
	trips = []
	for i in range(1,nnnn):
		for j in range(1,nnnn):
			for k in range(1,nnnn):
				if i + j + k == nnnn:
					one = [i, j, k]
					trips.append(one)
					print trips
	return trips

# print len(possibles(1000))
# print "end"

def triple(mmmm): # where mmmm is the target sum
	trips = []
	tester = []
	winner = []
	for a in range(1, mmmm):
		for b in range(1, mmmm):
			for c in range(1, mmmm):
				if a**2 + b **2 == c**2:
					winner = [a, b, c]
					trips.append(winner)
					print winner
	for i in range(len(trips)):
		tester = trips[i]
		if tester[0] + tester[1] + tester[2] == 1000:
			return tester[0] * tester[1] * tester[2]

print triple(1000)
