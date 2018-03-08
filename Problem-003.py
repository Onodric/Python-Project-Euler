import math


class Problem_003:
    """
    The prime factors of 13195 are 5, 7, 13, and 29.

    What is the largest prime factor of the number 600,851,475,143?
    """

    def is_prime(self, m):
        """
        Method to determine if a number is prime

        Arguments: <number> m
        Returns: m, if prime, "" if not
        """

        for i in range(2, m):
            if (m % i) == 0:
                return ""
        else:
            return m

    def get_largest_prime_of(self, n):
        """
        Method to calculate the largest prime factor of any given number

        Arguments: <number> n
        Returns: The largest prime factor of n
        """

        factors = []
        if n > 1:
            for entire_number in range(2, int(math.sqrt(n)) + 1):
                if (n % entire_number) == 0:
                    prime_or_nothing = self.is_prime(entire_number)
                    if prime_or_nothing == "":
                        """break"""
                    else:
                        factors.append(prime_or_nothing)
            return factors[-1]


if __name__ == "__main__":
    import sys
    solver = Problem_003()
    print(solver.get_largest_prime_of(int(sys.argv[1])))
