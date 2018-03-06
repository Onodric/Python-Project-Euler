# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def factorize(nnnnnn):
	factors = []
	for e in range(1,nnnnnn):
		if nnnnnn % e == 1:
			factors.append(e)
	return factors

# print factorize(997799)
# Factorize wasn't needed. But I guess I could have done it this way. I thought I could call this after testing 6-digit numbers from 999999 to 100000.
# That's a lot of numbers to search. So I did it the other way:

# define a function, no arguments, that finds the highest palindromic number that is the product of numbers from 900 to 999.
# this will print the two numbers and their product.
# would love to generalize this!
def products():
	# product = 0
	pal_test = [] # this is a list i use to store the digits of the product for testing ?palindromocity?
	for e in range(999, 900, -1):
		for i in range(999, 900, -1):
			product = e * i # the product of the number
			# print e, " * ",i , " = ", product # test print
			for x in range(len(str(product))): # a loop that runs the number times there are digits in the product.
				pal_test.append(str(product)[x]) # first add all the digits in
			if len(pal_test) > 5: # just realized that this needn't be in the above for loop.
				if pal_test[0] == pal_test[-1]:
					if pal_test[1] == pal_test[-2]:
						if pal_test[2] == pal_test[-3]:
							print e, " * ", i, " = "
							return product
			# print pal_test # test print
			product = 0
			pal_test = [] # reset both variables each time, esp. the list.
	return # the only return we care about is the one inside the ifs

print products()