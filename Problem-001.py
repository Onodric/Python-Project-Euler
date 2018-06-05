class Problem_001:
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    def sum_of_multiples(self, limit, multiple_1, multiple_2):
        """Finds the sum of all multiples of two numbers under a certain value

        Args:
            limit (integer): upper bound of multiples of `multiple_1` and
                `multiple_2`
            multiple_1 (integer): a base for multiple gathering
            multiple_2 (integer): a base for multiple gathering

        Returns:
            sum (integer): sum of all multiples of both `multiple_1` or
                `multiple_2` less then `limit`
        """

        sum = 0
        for e in range(limit):
            if e % multiple_1 == 0 or e % multiple_2 == 0:
                sum += e
        return sum


if __name__ == "__main__":
    import sys
    solver = Problem_001()
    print(solver.sum_of_multiples(
        int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
