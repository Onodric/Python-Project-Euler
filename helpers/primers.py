class Primers:
    """
    Helper class containing methods for finding primes
    Methods: is_prime(),
    """

    def is_prime(self, k):
        """
        Method to determine if a number is prime
        Arguments: <integer> k
        Returns: <boolean> is_prime
        """

        for i in range(2, k):
            if (k % i) == 0:
                return False
        return True
