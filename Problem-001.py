class Problem_001:
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    def sum_of_multiplpes(self, num, mult_1, mult_2):
        sum = 0
        for e in range(num):
            if e % mult_1 == 0 or e % mult_2 == 0:
                sum += e
        return sum


if __name__ == "__main__":
    import sys
    solver = Problem_001()
    print(solver.sum_of_multiplpes(
        int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
