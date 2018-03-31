class Problem_006:
    """
    The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
    """

    def get_sum_of_squares_of(self, n):
        """Finds the sum of all squares in the range 1 to n

        Args:
            n
        Returns:
            sum
        """

        total_sq = 0
        for e in range(1, n+1):
            total_sq += e*e
        return total_sq

    def get_square_of_sums_of(self, m):
        """Finds the square of the sum of all members in the range 1 to n

        Args:
            m
        Returns:
            square
        """

        sq_total = 0
        for i in range(1, m+1):
            sq_total += i
        return sq_total*sq_total


if __name__ == "__main__":
    import sys
    solver = Problem_006()
    print("The difference between the sum of squares and the square of sums in the range 1 to {} is {}".format(
        int(sys.argv[1]), solver.get_square_of_sums_of(int(sys.argv[1]))-solver.get_sum_of_squares_of(int(sys.argv[1]))))
