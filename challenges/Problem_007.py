from helpers.primers import Primers


class Problem_007:
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.
    What is the 10 001st prime number?
    """

    prime = Primers()

    def find_prime(self, m):
        """Finds the n-th prime

        Args:
            m
        Returns:
            nth prime
        """
        counter = 0
        num = 1
        while counter < m:
            num += 1
            if self.prime.is_prime(num):
                counter += 1
        return num

if __name__ == "__main__":
    import sys
    solver = Problem_007()
    print("The {}st prime is {}".format(int(sys.argv[1]), solver.find_prime(int(sys.argv[1]))))