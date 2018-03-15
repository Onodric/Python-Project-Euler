import math

class Factorize:
    """
    Class to assist in factoring
    Methods: get_all_prime_factors, getUniquePrimeFactors, getAllFactors
    """

    def get_all_prime_factors(self, n):
        """
        Method to return all prime factors of a number
        Arguments: <integer> n
        Returns: Array<integer> primeFactors
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

if __name__ == "__main__":
    import sys
    solver = Factorize()
    solved = solver.get_all_prime_factors(int(sys.argv[1]))
    print(solved)
