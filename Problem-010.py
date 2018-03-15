import functools
import math
from helpers import primers


class Problem_010:
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """

    all_primes = primers.Primers.get_all_primes_below

    def get_sum_of_primes_below(self, bounds):
        """
        Method to get the sum of all primes below a number
        Arguments: <integer> bounds
        Returns: <integer> Sum of all primes
        """
        primes = self.all_primes(bounds)
        return functools.reduce(lambda x, y: x+y, primes)

if __name__ == "__main__":
    import sys
    solver = Problem_010()
    arg = int(sys.argv[1])
