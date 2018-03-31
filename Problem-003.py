import math
import factorize as f

class Problem_003:
    """
    The prime factors of 13195 are 5, 7, 13, and 29.

    What is the largest prime factor of the number 600,851,475,143?
    """


    def get_largest_prime_factor_of(self, number):
        """Finds the largest prime factor of a given number

        Args:
            number
        Returns:
            The largest prime factor of n
        """

        factors = f.Factorize.get_all_prime_factors_of(number)
        factors.sort()
        return factors[-1]


if __name__ == "__main__":
    import sys
    solver = Problem_003()
    print(solver.get_largest_prime_factor_of(int(sys.argv[1])))
