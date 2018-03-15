from helpers.factorize import Factorize
from operator import mul
from functools import reduce


class Problem_005:
    """
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    """

    def getSmallestMultiple(self, n):
        """
        Method the returns the smallest even multiple of all the numbers below
                a maximum value (from 1 to n)
        Arguments: <integer> n
                Returns: <integer> multiple
        """

        help = Factorize()
        allFactors = help.get_all_prime_factors(n)

        for current in range(n-1, stop=2, step=-1):
            newFactors = help.get_all_prime_factors(current)
            for candidate in allFactors:
                try:
                    if newFactors.index(candidate):
                        newFactors.remove(candidate)
                except ValueError:
                    pass
                else:
                    pass
            allFactors = allFactors + newFactors
            allFactors.sort()
        return reduce(mul, allFactors, 1)

if __name__ == "__main__":
    import sys
    solver = Problem_005()
    print(solver.getSmallestMultiple(int(sys.argv[1])))