import math

class Factorize:
    """Assists in factoring

    Methods:
        get_all_prime_factors, getUniquePrimeFactors, getAllFactors
    """

    def get_all_prime_factors_of(self, n):
        """Finds all prime factors of a number

        Args:
            n: an integer o factor
        Returns:
            an array of all prime integer factors
        """

        primeFactors = []
        while n % 2 == 0:
            primeFactors.append(2)
            n /= 2
        for i in range(3, stop=math.floor(math.sqrt(n)), step=2):
            while n % i == 0:
                primeFactors.append(i)
                n /= i
        if n > 2:
            primeFactors.append(n)
        return primeFactors

    def get_all_factor_pairs_of(self, n):
        """Finds all factor pairs of a number

        Args:
            n: an integer to factor
        Returns:
            An array of all integer factors of a number
        """

        factors = []
        for e in range(1, int(math.sqrt(n)+1)):
            if n % e == 0:
                factors.append(e)
                factors.append(n/e)
        return factors

if __name__ == "__main__":
    import sys
    solver = Factorize()
    solved = solver.get_all_prime_factors_of(int(sys.argv[1]))
    print(solved)
