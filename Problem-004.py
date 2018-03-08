import math


class Problem_004:
    """
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """

    def find_largest_palidromic_product_of(self, magnitude):
        """
        Method to find the largest palindromic number that is a product of two
        n-digit numbers
        Arguments: <number> n
        Returns: <dictionary> results, containing the product and two n-digit
        numbers
        """

        largest = 10 ^ magnitude - 1
        smallest = 10 ^ (magnitude-1)
        for e in range(largest, smallest, -1):
            for i in range(largest, smallest, -1):
                pal_test = e * i
                middle = math.trunc(pal_test/2)
                place = 0
                while place < middle:
                    if pal_test[place] != pal_test[-(place+1)]:
                        break
                    else:
                        place += place
                results = dict()
                results.e = e
                results.i = i
                results.product = e*i
                return results
        return


if __name__ == "__main__":
    import sys
    solver = Problem_004()
    solved = solver.find_largest_palidromic_product_of(int(sys.argv[1]))
    print("The product of {} and {} is {}.".format(
        solved.e, solved.i, solved.product))
