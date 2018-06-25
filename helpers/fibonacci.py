class Fibonacci:
    """ A collection of methods for generating and manipulating Fibonacci sequences

    Methods:
        get_fibonacci_number
        get_fibonacci_numbers_under
    """

    def get_fibonacci_number(self, iteration):
        """Recursively finds a Fibonacci number

        Args:
            iteration (integer): the number of iterations (n)
        Returns:
            the Fibonacci number at iteration n
        """

        if iteration == 1 or iteration == 0:
            return iteration
        else:
            return self.get_fibonacci_number(iteration-1) + self.get_fibonacci_number(iteration-2)

    def get_fibonacci_numbers_under(self, limit):
        """Generates an array of Fibonacci numbers whose values are less than limit

        Recursive imlementation

        Args:
            limit (integer): the limit of the search function
        """

        fibonacci = [1, 1]
        while fibonacci[-1] < limit:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci


if __name__ == "__main__":
    import sys
    solver = Fibonacci()
    print(solver.get_fibonacci_number(int(sys.argv[1])))
