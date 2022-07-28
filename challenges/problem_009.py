class Problem_009:
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a2 + b2 = c2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    def get_pythagorean_trips_for(self, total):
        """
        Method to find Pythagorean triplets that sum to a given integer
        Arguments: <integer> total
        Returns: Array<Array<integer>> Pythagrean Triplet
        """
        trips = []
        for i in range(1, total-2):
            for j in range(1, total-2):
                for k in range(1, total-2):
                    if i + j + k == total:
                        one = [i, j, k]
                        trips.append(one)
        return trips

    def get_product_of_pyth_trips_summing_to(self, total):
        """
        Method to calculate the product of three numbers that are pytagorean triplets
        Arguments: <integer> total
        Return: <integer> product
        """
        trips = self.get_pythagorean_trips_for(total)
        products = []
        for i in range(len(trips)):
            tester = trips[i]
            if tester[0] + tester[1] + tester[2] == total:
                products.append(tester[0] * tester[1] * tester[2])
        return products


if __name__ == "__main__":
    import sys
    solver = Problem_009()
    arg = int(sys.argv[1])
    print("The products of all Pythagorean triples that sum to {} are:".format(arg))
    solutions = solver.get_product_of_pyth_trips_summing_to(arg)
    for i in range(len(solutions)):
        print("\t{}".format(solutions[i]))
