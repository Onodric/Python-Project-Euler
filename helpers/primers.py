class Primers:
    """
    Helper class containing methods for finding primes
    Methods: is_prime(), get_all_primes_below()
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

    def get_all_primes_below(self, bounds):
        """
        Returns a set of integer primes below the given value
        Arguments: <integer> bounds
        Returns: <number>()
        """

        primes = set()
        for i in range(2, bounds):
            if self.is_prime(i):
                primes.add(i)
        return primes
